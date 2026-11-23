# 《大模型推理系统与实践》

English repository slug: `intro-to-llm-inference-engines`

课程主页：[courses.sage.org.ai](https://courses.sage.org.ai/)

2027 年每位学生独立完成一个 MOD，个人项目得分即课程总评，满分 100 分。[考核与评分标准](src/site/tutorials/assessment/index.html)列出分项评分和各讲提交要求。[vLLM-HUST MOD 个人项目实验单](build/experiments/mod-project/vLLM-HUST_MOD_个人项目实验单.pdf)

**第 4 讲《开源实践与课程项目》开始制作 MOD。** 第 3 讲铺垫调度与 KV 抢占，随后用[第 4 讲 PPTX](build/slides/2027/lectures-8-pptx/第04讲_开源实践与课程项目.pptx)和 [MOD 开发教程](src/site/tutorials/mod/index.html#first-lab) 改 BidKV 策略并做 CPU 测试。第 5–7 讲支持插件联调与测量，第 8 讲比较实验结果并展示项目。[四次授课安排](src/docs/2027/课程安排.md) · [三套课件索引](build/slides/2027/README.md)

本仓库是《大模型推理系统与实践》课程材料的唯一维护与发布源，同时维护配套的 Nano-vLLM 教学代码与实验说明。个人主页和其他网站只提供到本仓库的引用，不再复制保存课件。所有版本的术语、算例、论文出处和课程边界以 `src/docs/2027/课程内容基线.md` 为准。

仓库现采用明确的 `src/` 与 `build/` 分层：`src/` 保存可维护的源文件与课程说明，`build/` 保存正式导出的 PPTX/PDF；外部页面直接引用本仓库中的发布件。

## 仓库内容

- `src/slides/lectures-14-beamer/`：14 讲细分版的 LaTeX Beamer 源码；`src/slides/Makefile` 是构建入口。
- `src/tutorials/`：tutorial Markdown 源码、Pandoc 过滤器与构建入口。
- `src/experiments/nano-vLLM实验课/`：Nano-vLLM 教学实验单与作业源文件。
- `src/experiments/mod-project/`：vLLM-HUST MOD 个人项目实验单源文件和打印样式。运行 `make -C src/experiments/mod-project` 以 Pandoc 和 Chromium 重新生成 PDF。
- `src/docs/`：课程简介、讲义提纲、教师讲稿与实验说明文档。
- `src/docs/2027/课程内容基线.md`：三套课件共同使用的正式名称、术语、算例、研究案例账本与讲次映射。
- `src/code/nano-vllm-hust/`：课程使用的 Nano-vLLM 教学 fork 与实验素材。
- `build/slides/2027/course-overview/`：中英文单文件课程介绍 PPTX，适合两小时快速介绍。
- `build/slides/2027/lectures-8-pptx/`：8 讲主课程版 PPTX，每讲对应 2 学时。
- `build/slides/2027/lectures-14-beamer/`：14 讲细分版 LaTeX Beamer 的正式 PDF 导出件。
- `build/slides/handouts/`：补充讲义导出件，不作为第四套课程入口。
- `build/tutorials/`：正式导出的 tutorial PDF。
- `build/experiments/`：正式导出的 experimental sheet / project sheet PDF。

## 使用建议

- 2027 年课程共 16 学时，分 4 次授课，每次 4 学时。8 讲 PPTX 与 14 讲 Beamer 按主题编号，实际授课按[课程安排](src/docs/2027/课程安排.md)选页与搭配实践。
- 需要修改 14 讲版时，进入 `src/slides/lectures-14-beamer/`；需要重新生成 PDF 时，在仓库根目录执行 `make` 或进入 `src/slides/` 执行 `make`。
- 理论讨论与知识问答优先参考 `src/tutorials/md/`。
- 代码实践、课程实验和作业说明优先参考 `src/code/nano-vllm-hust/` 与 `src/experiments/nano-vLLM实验课/`。
- `.preview/` 与 `.tectonic-cache/` 属于本地构建缓存，不作为长期维护内容。

## 维护原则

- 保持课程材料、实验说明和教学代码在同一仓库内同步演进。
- 对外只发布仓库链接；不得再向个人主页仓库复制 PPTX、PDF 或其他课程材料。
- 保持 `src/tutorials/` 与 `src/experiments/` 分工清楚：前者讲理论与问题，后者讲实验与操作。
- `src/code/` 目录以 `nano-vllm-hust/` 这一套教学代码为唯一主入口，不再保留额外的对照代码树作为课程仓库正式组成部分。
- 区分源文件与构建缓存，避免将本地 LaTeX 缓存作为正式内容提交。
- 若课程结构或实验组织方式发生变化，应同步更新本说明。

## 提交前清单

- 确认 `src/` 中只保留源文件，`build/` 中只保留正式导出的 PPTX/PDF。
- 确认 `src/tutorials/` 中不再承载详细实验课讲义，实验流程类文档统一放在 `src/experiments/`。
- 确认 `src/code/nano-vllm-hust/` 不再携带内层 `.git/` 元数据，避免提交成 gitlink。
- 确认 `.preview/`、`.tectonic-cache/` 以及 LaTeX 中间文件未进入待提交列表。
- 若调整了目录或文件名，同步检查 `README.md`、`src/docs/`、`src/tutorials/` 与 `src/experiments/` 中的路径说明是否仍然正确。
- 正式导出件统一位于 `build/`；LaTeX / Markdown 源码统一维护在 `src/`，本地临时构建产物不应混入提交。

## Agent 支持

本仓库现在提供一个专用 Copilot agent，用于处理课程讲义、tutorial、实验讲义和 nano-vLLM 教学代码之间的联动编辑：`.github/agents/intro-to-llm-inference-engines.agent.md`。
