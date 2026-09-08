import { createReadStream, existsSync, statSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { createServer } from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";

const sourceDir = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(sourceDir, "../..");
const outputDir = path.join(repositoryRoot, "dist");
const build = spawnSync(process.execPath, [path.join(sourceDir, "build.mjs")], { stdio: "inherit" });
if (build.status !== 0) process.exit(build.status ?? 1);

const types = { ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8" };
const server = createServer((request, response) => {
  const pathname = decodeURIComponent(new URL(request.url ?? "/", "http://localhost").pathname);
  const relative = pathname === "/" ? "index.html" : pathname.replace(/^\/+/, "");
  const requested = path.resolve(outputDir, relative);
  const candidate = existsSync(requested) && statSync(requested).isDirectory() ? path.join(requested, "index.html") : requested;
  const safe = candidate.startsWith(outputDir + path.sep) && existsSync(candidate) && statSync(candidate).isFile();
  const file = safe ? candidate : path.join(outputDir, "index.html");
  response.writeHead(safe || pathname === "/" ? 200 : 404, { "Content-Type": types[path.extname(file)] ?? "application/octet-stream" });
  createReadStream(file).pipe(response);
});

server.listen(4173, "127.0.0.1", () => console.log("Local: http://127.0.0.1:4173/"));
