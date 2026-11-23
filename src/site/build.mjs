import { cp, mkdir, readdir, readFile, rm, stat, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const sourceDir = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(sourceDir, "../..");
const outputDir = path.join(repositoryRoot, "dist");

await rm(outputDir, { recursive: true, force: true });
await mkdir(outputDir, { recursive: true });

for (const file of ["index.html", "styles.css"]) {
  await cp(path.join(sourceDir, file), path.join(outputDir, file));
}

await cp(path.join(sourceDir, "assets"), path.join(outputDir, "assets"), { recursive: true });
await cp(path.join(sourceDir, "tutorials"), path.join(outputDir, "tutorials"), { recursive: true });

const downloadGroups = [
  { id: "mod-project", title: "个人项目实验单", source: "build/experiments/mod-project", extensions: [".pdf"] },
  { id: "overview", title: "两小时课程介绍", source: "build/slides/2027/course-overview", extensions: [".pptx"] },
  { id: "lectures", title: "八讲主课程", source: "build/slides/2027/lectures-8-pptx", extensions: [".pptx"] },
];

const downloadLabels = new Map([
  ["vLLM-HUST_MOD_个人项目实验单.pdf", "vLLM-HUST MOD 个人项目实验单"],
  ["LLM推理系统_两小时快速介绍.pptx", "中文课程介绍"],
  ["llm_inference_systems.pptx", "英文课程介绍"],
  ["第02讲_请求生命周期与PrefillDecode.pptx", "第 2 讲 · 请求生命周期与 Prefill / Decode"],
  ["第05讲_MOD实现与CPU测试.pptx", "第 5 讲 · MOD 实现与 CPU 测试"],
  ["第06讲_MOD打包与宿主联调.pptx", "第 6 讲 · MOD 打包与宿主联调"],
  ["第07讲_MOD对照评测与结果分析.pptx", "第 7 讲 · MOD 对照评测与结果分析"],
  ["第08讲_MOD复现验收与个人答辩.pptx", "第 8 讲 · MOD 复现验收与个人答辩"],
]);

const courseRepository = "https://github.com/vLLM-HUST/intro-to-llm-inference-engines";
const repositoryOnlyLectures = new Set([
  "第04讲_开源实践与课程项目.pptx",
  "第08讲_MOD复现验收与个人答辩.pptx",
]);

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
  const files = await collectFiles(absoluteSource, group.extensions);
  const renderedFiles = [];
  for (const sourceFile of files) {
    const relative = path.relative(path.join(repositoryRoot, "build"), sourceFile);
    const filename = path.basename(sourceFile);
    const fromRepository = group.id === "lectures" && repositoryOnlyLectures.has(filename);
    const encodedPath = relative.split(path.sep).map(encodeURIComponent).join("/");
    if (!fromRepository) {
      const destination = path.join(publicRoot, relative);
      await mkdir(path.dirname(destination), { recursive: true });
      await cp(sourceFile, destination);
    }
    const bytes = (await stat(sourceFile)).size;
    const title = downloadLabels.get(filename) ?? path.basename(filename, path.extname(filename))
      .replaceAll("_", " ")
      .replace(/^第0?([1-8])讲 /, "第 $1 讲 · ");
    renderedFiles.push({
      href: fromRepository ? `${courseRepository}/blob/main/build/${encodedPath}` : encodedPath,
      label: title,
      format: path.extname(sourceFile).slice(1).toUpperCase(),
      sourceLabel: fromRepository ? "GitHub" : `${(bytes / 1024 / 1024).toFixed(1)} MB`,
      fromRepository,
    });
  }
  renderedGroups.push({ ...group, files: renderedFiles });
}

const downloadSections = renderedGroups.map((group) => `
    <section class="download-group" id="${group.id}">
      <div class="download-heading"><h2>${escapeHtml(group.title)}</h2></div>
      <div class="download-list">
        ${group.files.map((file) => `<a href="${file.href}"${file.fromRepository ? "" : " download"}><strong>${escapeHtml(file.label)}</strong><span>${file.format} · ${file.sourceLabel}</span></a>`).join("\n        ")}
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
  <a class="skip-link" href="#main">跳到课程材料</a>
  <header class="site-header"><a class="brand" href="../"><span class="brand-mark" aria-hidden="true">IS</span><span><strong>LLM Inference</strong><small>Systems &amp; Practice</small></span></a><a class="header-link" href="../">返回课程主页</a></header>
  <main class="downloads-main" id="main">
    <div class="downloads-intro"><h1>课程材料下载</h1></div>
    ${downloadSections}
  </main>
  <footer><p>《大模型推理系统与实践》 · 华中科技大学计算机学院 · 张书豪</p></footer>
</body>
</html>`;

await writeFile(path.join(publicRoot, "index.html"), downloadsPage, "utf8");

if (process.env.COURSE_SITE_URL) {
  const baseURL = new URL(process.env.COURSE_SITE_URL);
  if (baseURL.protocol !== "https:" || baseURL.username || baseURL.password || baseURL.search || baseURL.hash) {
    throw new Error("COURSE_SITE_URL must be an HTTPS site URL");
  }
  const canonicalRoot = baseURL.href.replace(/\/?$/, "/");
  for (const file of await collectFiles(outputDir, [".html"])) {
    const markup = await readFile(file, "utf8");
    const updated = markup.replace(
      'rel="canonical" href="https://courses.sage.org.ai/',
      () => `rel="canonical" href="${escapeHtml(canonicalRoot)}`,
    );
    await writeFile(file, updated, "utf8");
  }
}

console.log(`Course site built in ${outputDir} with ${renderedGroups.reduce((sum, group) => sum + group.files.filter((file) => !file.fromRepository).length, 0)} public downloads`);
