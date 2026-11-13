"""Run the RIDE Controller concurrency and lifecycle demo on one CPU machine."""

from concurrent.futures import ThreadPoolExecutor
from http import HTTPStatus
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
from threading import Event, Thread
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

from ride.mock_vllm import server as mock_server


def http_json(url, payload=None):
    if payload is None:
        request = Request(url)
    else:
        request = Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
        )
    with urlopen(request) as response:
        return json.load(response)


def unused_port():
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        return listener.getsockname()[1]


def wait_for(observe, condition, description):
    # This deadline only bounds the demo's status checks.
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline:
        try:
            value = observe()
        except URLError:
            time.sleep(0.05)
            continue
        if condition(value):
            return value
        time.sleep(0.05)
    raise RuntimeError(f"Did not observe {description}")


def main():
    release_backend = Event()
    with tempfile.TemporaryDirectory(prefix="ride-demo-") as directory, mock_server(
        "127.0.0.1", 0
    ) as backend:
        workspace = Path(directory).name
        backend_url = f"http://127.0.0.1:{backend.server_port}"
        original_handler = backend.RequestHandlerClass

        class DelayedMockHandler(original_handler):
            def do_POST(self):
                # Hold the first forwarded request so the queue can be observed.
                if release_backend.wait(20):
                    super().do_POST()
                else:
                    self.send_error(HTTPStatus.SERVICE_UNAVAILABLE)

        backend.RequestHandlerClass = DelayedMockHandler
        Thread(target=backend.serve_forever, daemon=True).start()

        management_port = unused_port()
        controller_port = unused_port()
        while controller_port == management_port:
            controller_port = unused_port()
        management_url = f"http://127.0.0.1:{management_port}"
        controller_url = f"http://127.0.0.1:{controller_port}"
        controller = "tutorial-concurrency-demo"

        def ride(*arguments):
            result = subprocess.check_output(
                [sys.executable, "-m", "ride", *arguments, "--address", management_url],
                text=True,
            )
            return json.loads(result)

        def describe():
            return ride("describe", "controller", controller)

        def generate():
            response = http_json(
                controller_url + "/v1/chat/completions",
                {
                    "model": "mock-vllm",
                    "messages": [{"role": "user", "content": "hello"}],
                    "stream": False,
                },
            )
            if response["choices"][0]["message"]["content"] != "hello":
                raise RuntimeError(f"Unexpected mock response: {response}")
            return "hello"

        def status():
            return http_json(controller_url + "/status")

        def show(label, value):
            print(f"{label}: {json.dumps(value, ensure_ascii=False)}", flush=True)

        config = Path(directory, "controller.json")
        config.write_text(json.dumps({"listen": f"127.0.0.1:{controller_port}"}))
        started = False
        with subprocess.Popen(
            [
                sys.executable, "-m", "ride", "start", "--executor", "local",
                "--workspace", workspace, "--listen", f"127.0.0.1:{management_port}",
                "--state-file", str(Path(directory, "state.json")),
            ],
            stdout=subprocess.PIPE, text=True,
        ) as management:
            try:
                # The management process prints its identity after binding the port.
                if json.loads(management.stdout.readline())["workspace"] != workspace:
                    raise RuntimeError("Unexpected RIDE management identity")

                first = ride(
                    "start", "controller", "demo", "--name", controller,
                    "--config", str(config), "--backend", backend_url,
                    "--endpoint", controller_url,
                )
                started = True
                ready = wait_for(describe, lambda value: value["ready"], "Controller Ready")
                show("ready", {"max_concurrency": ready["identity"]["max_concurrency"]})
                with ThreadPoolExecutor(max_workers=4) as pool:
                    requests = [pool.submit(generate) for _ in range(4)]
                    try:
                        queued = wait_for(
                            status, lambda value: value["active"] == 1 and value["waiting"] == 3,
                            "one active request and three waiting",
                        )
                        show("while waiting", {"active": queued["active"], "waiting": queued["waiting"]})
                    finally:
                        release_backend.set()
                    show("responses", [request.result() for request in requests])

                expected = {
                    "active": 0, "waiting": 0, "completed": 4,
                    "failed": 0, "peak_active": 1, "queued_total": 3,
                }
                final = wait_for(status, lambda value: value == expected, "all four requests completed")
                show("after completion", final)

                ride("stop", "controller", controller)
                stopped = wait_for(
                    describe, lambda value: value["job_status"] == "STOPPED", "Controller STOPPED"
                )
                show("after stop", {
                    "controller": stopped["job_status"],
                    "model": http_json(backend_url + "/health")["status"],
                })

                restored = ride("start", "controller", controller)
                wait_for(describe, lambda value: value["ready"], "restored Controller Ready")
                if restored["job_id"] == first["job_id"]:
                    raise RuntimeError("Expected a new Controller Job ID after restart")
                show("after restart", {"new_job_id": True, "response": generate()})
            finally:
                release_backend.set()
                try:
                    if started:
                        ride("stop", "controller", controller)
                finally:
                    management.terminate()
                    backend.shutdown()


if __name__ == "__main__":
    main()
