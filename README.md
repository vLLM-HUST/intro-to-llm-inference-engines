# 《大模型推理引擎入门》

English repository slug: `intro-to-llm-inference-engines`

本仓库用于集中维护“大模型推理基础设施”课程相关授课材料，以及配套的 Nano-vLLM 教学代码与实验说明。

## 仓库内容

- `slides/`：课程讲义导出 PDF 与课件输出目录
- `slides/tex/`：逐讲课件与讲义的 LaTeX 源码
- `slides/Makefile`：将 `slides/tex/` 下源码编译到 `slides/` 的最小构建入口
- `docs/`：课程简介、讲义提纲、教师讲稿与实验说明文档
- `code/nano-vllm-hust/`：课程使用的 Nano-vLLM 教学 fork 与实验素材
- `tutorials/nano-vLLM实验与Tutorials/`：面向学生的理论导学、知识问答与课堂讨论文档
- `experiments/nano-vLLM实验课/`：面向学生的详细实验课讲义与课程项目实验文档

## 使用建议

- 日常授课内容优先参考 `slides/` 下的导出 PDF，以及 `docs/` 中的讲义和说明文档。
- 需要修改课件源码时，进入 `slides/tex/`；需要重新生成 PDF 时，在 `slides/` 下执行 `make`。
- 理论讨论与知识问答优先参考 `tutorials/nano-vLLM实验与Tutorials/`。
- 代码实践、课程实验和作业说明优先参考 `code/nano-vllm-hust/` 与 `experiments/nano-vLLM实验课/`。
- `.preview/` 与 `.tectonic-cache/` 属于本地构建缓存，不作为长期维护内容。

## 维护原则

- 保持课程材料、实验说明和教学代码在同一仓库内同步演进。
- 保持 `tutorials/` 与 `experiments/` 分工清楚：前者讲理论与问题，后者讲实验与操作。
- `code/` 目录以 `nano-vllm-hust/` 这一套教学代码为唯一主入口，不再保留额外的对照代码树作为课程仓库正式组成部分。
- 区分源文件与构建缓存，避免将本地 LaTeX 缓存作为正式内容提交。
- 若课程结构或实验组织方式发生变化，应同步更新本说明。

## 提交前清单

- 确认 `slides/`、`docs/`、`code/`、`tutorials/` 与 `experiments/` 五层结构没有被重新打散。
- 确认 `tutorials/` 中不再承载详细实验课讲义，实验流程类文档统一放在 `experiments/`。
- 确认 `code/nano-vllm-hust/` 不再携带内层 `.git/` 元数据，避免提交成 gitlink。
- 确认 `.preview/`、`.tectonic-cache/` 以及 LaTeX 中间文件未进入待提交列表。
- 若调整了目录或文件名，同步检查 `README.md`、`docs/` 与 `tutorials/` 中的路径说明是否仍然正确。
- 仅在需要保留课程导出件时提交 `slides/` 下 PDF；LaTeX 源码统一维护在 `slides/tex/`，本地临时构建产物不应混入提交。
