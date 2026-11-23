# 《大模型推理系统与实践》

English repository slug: `intro-to-llm-inference-engines`

[课程网站](https://courses.sage.org.ai/) · [2027 年授课安排](src/docs/2027/课程安排.md) · [八讲课件](build/slides/2027/README.md)

2027 年每位学生必做一个 vLLM-HUST 引擎 MOD，基础成绩满分 100 分。为 yancan 负责的 Control Plane 另做一个 RIDE Controller 插件最多加 30 分。[考核与评分标准](src/site/tutorials/assessment/index.html) · [vLLM-HUST MOD 个人项目实验单](build/experiments/mod-project/vLLM-HUST_MOD_个人项目实验单.pdf)

学生可从 [vLLM-HUST 引擎 MOD 模板](https://github.com/vLLM-HUST/vllm-hust-mod-template)和 [RIDE Controller 模板](https://github.com/vLLM-HUST/ride-controller-template)创建个人项目仓库。

**第 4 讲《开源实践与课程项目》开始制作 MOD。** 第 3 讲铺垫调度与 KV 抢占，随后用[第 4 讲 PPTX](build/slides/2027/lectures-8-pptx/第04讲_开源实践与课程项目.pptx)和 [MOD 开发教程](src/site/tutorials/mod/index.html#first-lab) 改 BidKV 策略并做 CPU 测试。第 5–7 讲支持插件联调与测量，第 8 讲比较实验结果并展示项目。[四次授课安排](src/docs/2027/课程安排.md) · [课件索引](build/slides/2027/README.md)

本仓库维护《大模型推理系统与实践》的正式课件、MOD 项目实验单和课程网站。术语、算例、论文出处和课程边界见[课程内容基线](src/docs/2027/课程内容基线.md)。

仓库现采用明确的 `src/` 与 `build/` 分层：`src/` 保存可维护的源文件与课程说明，`build/` 保存正式导出的 PPTX/PDF；外部页面直接引用本仓库中的发布件。

## 仓库内容

- `src/site/tutorials/mod/`：vLLM-HUST MOD 开发教程。
- `src/experiments/mod-project/`：vLLM-HUST MOD 个人项目实验单源文件和打印样式。运行 `make -C src/experiments/mod-project` 以 Pandoc 和 Chromium 重新生成 PDF。
- `src/docs/`：课程简介、授课安排与内容基线。
- `build/slides/2027/course-overview/`：中英文单文件课程介绍 PPTX，适合两小时快速介绍。
- `build/slides/2027/lectures-8-pptx/`：8 讲主课程版 PPTX，每讲对应 2 学时。
- `build/experiments/mod-project/`：个人 MOD 项目实验单 PDF。

## 使用建议

- 2027 年课程共 16 学时，分 4 次授课，每次 4 学时。随[课程安排](src/docs/2027/课程安排.md)使用八讲 PPTX 和个人 MOD 项目材料。
- [RIDE Control Plane 教程](src/site/tutorials/ride/index.html)用于可选的 Controller 插件加分项目。
- `.preview/` 与 `.tectonic-cache/` 属于本地构建缓存，不作为长期维护内容。

## 维护原则

- 对照更新课件、课程安排、MOD 教程、实验单和考核标准。
- 对外只发布仓库链接；不得再向个人主页仓库复制 PPTX、PDF 或其他课程材料。
- 区分源文件与构建缓存，避免将本地 LaTeX 缓存作为正式内容提交。
- 若课程结构或实验组织方式发生变化，应同步更新本说明。

## 提交前清单

- 确认 `src/` 中只保留源文件，`build/` 中只保留正式导出的 PPTX/PDF。
- 确认 `.preview/`、`.tectonic-cache/` 以及 LaTeX 中间文件未进入待提交列表。
- 若调整了目录或文件名，同步检查课程安排、项目实验单和网站下载入口。
- 正式导出件统一位于 `build/`；LaTeX / Markdown 源码统一维护在 `src/`，本地临时构建产物不应混入提交。
