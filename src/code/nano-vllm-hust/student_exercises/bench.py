import csv
import os
import time
from random import randint, seed

from nanovllm import LLM, SamplingParams


def build_workload(num_seqs: int, max_input_len: int, max_output_len: int):
    """Tutorial 5 task.

    Goal:
    - generate prompt token ids with variable input length
    - generate one SamplingParams per request
    - keep the workload deterministic under `seed(0)`
    """
    raise NotImplementedError("TODO: implement deterministic benchmark workload builder")


def append_result(csv_path: str, row: dict):
    """Tutorial 5 task.

    Goal:
    - create the parent directory when needed
    - append one structured CSV row
    - write the header on first use only
    """
    raise NotImplementedError("TODO: implement structured result logging")


def main():
    seed(0)
    num_seqs = 256
    max_input_len = 1024
    max_output_len = 1024

    path = os.path.expanduser("~/huggingface/Qwen3-0.6B/")
    llm = LLM(path, enforce_eager=False, max_model_len=4096)

    prompt_token_ids, sampling_params = build_workload(num_seqs, max_input_len, max_output_len)

    llm.generate(["Benchmark: "], SamplingParams())
    t0 = time.time()
    llm.generate(prompt_token_ids, sampling_params, use_tqdm=False)
    elapsed = time.time() - t0
    total_tokens = sum(sp.max_tokens for sp in sampling_params)
    throughput = total_tokens / elapsed

    result = {
        "num_seqs": num_seqs,
        "max_input_len": max_input_len,
        "max_output_len": max_output_len,
        "elapsed": f"{elapsed:.4f}",
        "total_tokens": total_tokens,
        "throughput": f"{throughput:.4f}",
    }
    append_result("results/tutorial5_benchmark.csv", result)
    print(result)


if __name__ == "__main__":
    main()
