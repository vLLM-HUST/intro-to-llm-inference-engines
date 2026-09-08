import { cp, mkdir, rm } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const sourceDir = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(sourceDir, "../..");
const outputDir = path.join(repositoryRoot, "dist");

await rm(outputDir, { recursive: true, force: true });
await mkdir(outputDir, { recursive: true });

for (const file of ["index.html", "styles.css", "app.js"]) {
  await cp(path.join(sourceDir, file), path.join(outputDir, file));
}

console.log(`Course site built in ${outputDir}`);
