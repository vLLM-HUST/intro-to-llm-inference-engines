# nano-vLLM Tutorials 总览

## 定位

这组材料现在专门承担《大模型推理基础设施》课程中的理论导学任务。它们不再承担详细实验课讲义的职责，而是围绕每个主题组织概念辨析、课堂问答、阅读提示和推理链路训练。

如果要做代码操作、插桩、结果记录和提交，请进入 `experiments/nano-vLLM实验课/`。

## 使用方式

建议把这组材料作为“讲义之后、实验之前”的过渡层：

- 课上先用 `slides/` 下的导出 PDF、`slides/tex/` 下的源码和 `docs/` 讲清系统问题。
- 再用本目录的 tutorial 组织理论问答、概念辨析和代码职责判断。
- 最后进入 `experiments/nano-vLLM实验课/` 做详细实验课。

课程节奏不是把 tutorial 当成独立副线，而是先在前 6 讲讲清概念，再在第 7-11 讲用 tutorial 把同一个问题回放到最小 runtime 上。

## 与 experiments 的分工

| 材料类型 | 主要作用 | 典型产出 |
| --- | --- | --- |
| Tutorials | 理论问答、概念辨析、阅读提示、代码职责判断 | 问答记录、概念图、因果链、职责表 |
| Experiments | 实验步骤、插桩位置、运行记录、提交模板 | 日志、结果表、时序图、实验报告 |

## 使用前提

当前课程已经配套提供教学 fork `code/nano-vllm-hust`。教师可以优先基于该仓库授课；如果后续替换成别的最小 runtime，本套材料仍可按“职责映射”迁移。正式布置时，优先把下列职责映射到 `code/nano-vllm-hust` 的对应代码：

- 最小运行入口：`example.py`
- 用户 API 与请求构造：`nanovllm/llm.py`
- 请求主路径：`nanovllm/engine/llm_engine.py`
- 调度循环：`nanovllm/engine/scheduler.py`
- 执行器：`nanovllm/engine/model_runner.py`
- KV 与状态组织：`nanovllm/engine/block_manager.py`、`nanovllm/engine/sequence.py`
- benchmark：`bench.py`
- 学生练习与交付模板：`student_exercises/`、`assignments/`
- 助教脚本：`scripts/teaching/prepare_assignment.py`、`scripts/teaching/collect_benchmark_results.py`

如果教学版 nano-vLLM 的文件名不同，按职责替换即可，不影响实验目标。

## Tutorials 结构

1. `Tutorial_01_最小运行与代码地图.md`
   目标：让学生回答一次请求从哪里进入系统，以及为什么“代码地图”是后续实验的必要前提。
2. `Tutorial_02_请求生命周期与PrefillDecode.md`
   目标：让学生辨析请求生命周期中的阶段边界，以及 prefill/decode 为什么不能混成同一种任务。
3. `Tutorial_03_调度与连续批处理观察.md`
   目标：让学生回答调度器究竟控制了什么，以及连续批处理的收益和代价来自哪里。
4. `Tutorial_04_KV_Cache与状态组织.md`
   目标：让学生把 KV 理解为状态对象，而不是临时变量，并建立“状态 -> 并发/等待 -> 指标”的因果链。
5. `Tutorial_05_指标观测与最小复现实验.md`
   目标：让学生回答什么是可信实验，什么只是观测现象。

## 推荐交付节奏

- Tutorial 1：提交一张代码职责表和一段“第一个控制点”判断。
- Tutorial 2：提交一张生命周期概念图和一份 prefill/decode 区分说明。
- Tutorial 3：提交一份调度 trade-off 问答记录。
- Tutorial 4：提交一条状态因果链和一份状态对象辨析说明。
- Tutorial 5：提交一份实验可信性检查表。

## 教师使用建议

- 不要求学生第一次就看完所有代码，先盯住一条最短控制路径。
- 每个 tutorial 只要求学生回答一个核心问题，避免变成隐藏版实验说明。
- tutorial 中尽量少放命令、少放逐步操作，多放反例、边界和追问。
- 详细实验流程统一放到 `experiments/`，不要再写回 tutorial。
- 讲课时同时指出“本页概念对应哪个 tutorial 和哪节实验课”，让学生知道理论和实践如何接续。

## 统一产出规范

每次 tutorial 或实验报告建议固定包含五部分：

1. 本次要回答的系统问题。
2. 相关代码职责与调用路径。
3. 修改或插桩位置。
4. 结果表格或日志摘要。
5. 哪个结果会直接否定当前解释。

这套规范的目的是把“读代码”“跑实验”“写项目”统一到同一套系统研究语言中。