import { cp, mkdir, readdir, rm, stat, writeFile } from "node:fs/promises";
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

await cp(path.join(sourceDir, "assets"), path.join(outputDir, "assets"), { recursive: true });

const downloadGroups = [
  { id: "overview", title: "两小时快速介绍", source: "build/slides/2027/course-overview", extensions: [".pptx"] },
  { id: "lectures", title: "八讲主课程", source: "build/slides/2027/lectures-8-pptx", extensions: [".pptx"] },
  { id: "beamer", title: "详细课件", source: "build/slides/2027/lectures-14-beamer", extensions: [".pdf"] },
];

async function collectFiles(directory, extensions) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await collectFiles(absolute, extensions));
    if (entry.isFile() && extensions.includes(path.extname(entry.name).toLowerCase())) files.push(absolute);
  }
  return files.sort((a, b) => a.localeCompare(b, "zh-CN", { numeric: true }));
}

const escapeHtml = (value) => value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
const publicRoot = path.join(outputDir, "downloads");
const renderedGroups = [];

for (const group of downloadGroups) {
  const absoluteSource = path.join(repositoryRoot, group.source);
  const files = (await collectFiles(absoluteSource, group.extensions)).filter((file) => {
    const name = path.basename(file);
    if (group.id === "lectures" && /^第(07|08)讲_/.test(name)) return false;
    if (group.id === "beamer" && /第(11|12|13)讲_/.test(name)) return false;
    return true;
  });
  const renderedFiles = [];
  for (const sourceFile of files) {
    const relative = path.relative(path.join(repositoryRoot, "build"), sourceFile);
    const destination = path.join(publicRoot, relative);
    await mkdir(path.dirname(destination), { recursive: true });
    await cp(sourceFile, destination);
    const bytes = (await stat(sourceFile)).size;
    const baseLabel = path.basename(sourceFile, path.extname(sourceFile));
    const label = baseLabel === "sheet" ? path.basename(path.dirname(sourceFile)) : baseLabel;
    renderedFiles.push({
      href: relative.split(path.sep).map(encodeURIComponent).join("/"),
      label: label.replaceAll("_", " "),
      format: path.extname(sourceFile).slice(1).toUpperCase(),
      size: `${(bytes / 1024 / 1024).toFixed(1)} MB`,
    });
  }
  renderedGroups.push({ ...group, files: renderedFiles });
}

const downloadSections = renderedGroups.map((group) => `
    <section class="download-group" id="${group.id}">
      <div class="download-heading"><h2>${escapeHtml(group.title)}</h2><span>${group.files.length} 份文件</span></div>
      <div class="download-list">
        ${group.files.map((file) => `<a href="${file.href}" download><strong>${escapeHtml(file.label)}</strong><span>${file.format} · ${file.size} ↓</span></a>`).join("\n        ")}
      </div>
    </section>`).join("\n");

const downloadsPage = `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>课程材料下载｜大模型推理系统与实践</title>
  <meta name="description" content="《大模型推理系统与实践》公开 PPTX 与 PDF 下载。">
  <link rel="canonical" href="https://courses.sage.org.ai/downloads/">
  <link rel="stylesheet" href="../styles.css">
</head>
<body class="downloads-page">
  <header class="site-header"><a class="brand" href="../"><span class="brand-mark" aria-hidden="true">IS</span><span><strong>LLM Inference</strong><small>Systems &amp; Practice</small></span></a><a class="header-link" href="../">返回课程主页</a></header>
  <main class="downloads-main">
    <section class="downloads-intro"><p class="eyebrow">Public course materials</p><h1>课程材料下载</h1><p>下载课程课件和阅读材料。</p></section>
    ${downloadSections}
  </main>
  <footer><p>《大模型推理系统与实践》 · 华中科技大学计算机学院 · 张书豪</p></footer>
</body>
</html>`;

await writeFile(path.join(publicRoot, "index.html"), downloadsPage, "utf8");

console.log(`Course site built in ${outputDir} with ${renderedGroups.reduce((sum, group) => sum + group.files.length, 0)} public downloads`);
