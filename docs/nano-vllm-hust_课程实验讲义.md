# nano-vllm-hust 课程实验讲义

## 一、实验讲义定位

本讲义配合“大模型推理基础设施”课程使用，目标是把课堂中讲解的请求生命周期、调度、KV 状态管理与实验验证方法，落实到 `code/nano-vllm-hust` 这一教学代码库中。

该代码库同时包含两层内容：

- `code/nano-vllm-hust/nanovllm/`：可直接运行的参考实现，用于课堂导读与教师演示。
- `code/nano-vllm-hust/student_exercises/`：带 TODO 的教学练习版本，用于课程实验与作业提交。

## 二、实验总体目标

学生完成本组实验后，应具备以下能力：

- 能够沿主路径解释一次请求如何进入、执行并完成。
- 能够说明调度器如何在 prefill 与 decode 阶段组织请求。
- 能够解释 KV block 的分配、复用、哈希与回收过程。
- 能够把一次 benchmark 运行整理为可复现的实验记录。

## 三、代码结构与课程映射

### 0. 课程闭环总表

建议教师和学生都先看这张表，再进入单次实验。这样每个人都能清楚知道同一个知识点在讲义、tutorial、实验和代码里分别落在哪里。

| 对应讲次 | tutorial / 实验 | 参考实现 | 学生练习与作业包 | 主要交付 |
| --- | --- | --- | --- | --- |
| 第 1-2 讲 | Tutorial 1 / `experiments/nano-vLLM实验课/实验一_最小运行与代码地图.md` | `code/nano-vllm-hust/example.py`、`code/nano-vllm-hust/nanovllm/llm.py`、`code/nano-vllm-hust/nanovllm/engine/llm_engine.py` | `code/nano-vllm-hust/assignments/tutorial_1_spring-2026/` | 代码地图、最短调用链、最小日志 |
| 第 3 讲 | Tutorial 2 / `experiments/nano-vLLM实验课/实验二_请求生命周期观察.md` | `code/nano-vllm-hust/nanovllm/engine/llm_engine.py`、`code/nano-vllm-hust/nanovllm/engine/sequence.py` | `code/nano-vllm-hust/student_exercises/nanovllm/engine/llm_engine.py`、`code/nano-vllm-hust/assignments/tutorial_2_spring-2026/` | 生命周期时序图、长短 prompt 对比表 |
| 第 4 讲 | Tutorial 3 / `experiments/nano-vLLM实验课/实验三_调度与连续批处理实验.md` | `code/nano-vllm-hust/nanovllm/engine/scheduler.py` | `code/nano-vllm-hust/student_exercises/nanovllm/engine/scheduler.py`、`code/nano-vllm-hust/assignments/tutorial_3_spring-2026/` | batch 观测日志、调度对比表 |
| 第 5-6 讲 | Tutorial 4 / `experiments/nano-vLLM实验课/实验四_KV状态与缓存组织实验.md` | `code/nano-vllm-hust/nanovllm/engine/block_manager.py`、`code/nano-vllm-hust/nanovllm/engine/sequence.py` | `code/nano-vllm-hust/student_exercises/nanovllm/engine/block_manager.py`、`code/nano-vllm-hust/assignments/tutorial_4_spring-2026/` | KV 生命周期图、状态容量分析 |
| 第 11 讲 | Tutorial 5 / `experiments/nano-vLLM实验课/实验五_指标观测与最小复现实验.md` | `code/nano-vllm-hust/bench.py` | `code/nano-vllm-hust/student_exercises/bench.py`、`code/nano-vllm-hust/assignments/tutorial_5_spring-2026/` | 最小复现实验包、结果表、边界说明 |

### 1. 请求生命周期

- 参考文件：`code/nano-vllm-hust/nanovllm/engine/llm_engine.py`
- 对应课程讲次：第 3 讲“请求生命周期”
- 核心问题：请求从哪里进入？在哪一步完成调度、执行和输出汇总？

建议阅读重点：

- `add_request()` 如何构造 `Sequence`
- `step()` 如何串联调度、执行与后处理
- `generate()` 如何驱动全局循环直到全部请求完成

### 2. 调度控制

- 参考文件：`code/nano-vllm-hust/nanovllm/engine/scheduler.py`
- 对应课程讲次：第 4 讲“请求调度”
- 核心问题：调度器如何区分 waiting 和 running？何时发生抢占？

建议阅读重点：

- `schedule()` 中的 prefill/decode 分支
- `preempt()` 如何触发状态回退
- `postprocess()` 如何同步更新运行态和完成态

### 3. KV 状态管理

- 参考文件：`code/nano-vllm-hust/nanovllm/engine/block_manager.py`
- 对应课程讲次：第 5 讲“KV 缓存”和第 6 讲“状态管理”
- 核心问题：块如何被分配、共享、哈希和回收？

建议阅读重点：

- `can_allocate()` 的缓存命中估算逻辑
- `allocate()` / `deallocate()` 的块生命周期逻辑
- `hash_blocks()` 如何把完整块写入哈希表

### 4. 状态对象建模

- 参考文件：`code/nano-vllm-hust/nanovllm/engine/sequence.py`
- 对应课程讲次：第 6 讲“状态管理与记忆组织”
- 核心问题：一个请求对象如何同时承载 token、调度状态和 KV 元数据？

建议阅读重点：

- `status`、`num_cached_tokens`、`block_table`
- `num_blocks`、`last_block_num_tokens`
- `__getstate__()` / `__setstate__()` 的状态序列化含义

### 5. 实验记录与结果整理

- 参考文件：`code/nano-vllm-hust/bench.py`
- 对应课程讲次：第 11 讲“实验方法与验证”
- 核心问题：怎样把一次运行转化为可比较、可复现的实验结果？

建议阅读重点：

- 随机种子与输入长度分布的控制方式
- warmup 的作用
- 总 token、总时间与 throughput 的计算方法

## 四、建议实验顺序

建议按以下顺序完成实验，而不要跳跃式阅读：

1. 先运行 `code/nano-vllm-hust/example.py`，再阅读 `code/nano-vllm-hust/nanovllm/llm.py` 和 `code/nano-vllm-hust/nanovllm/engine/llm_engine.py`，建立最小请求路径。
2. 阅读 `code/nano-vllm-hust/nanovllm/engine/llm_engine.py` 和 `code/nano-vllm-hust/nanovllm/engine/sequence.py`，画出一次请求的生命周期图。
3. 再阅读 `code/nano-vllm-hust/nanovllm/engine/scheduler.py`，解释 waiting、running 和 preempt 的状态转移。
4. 接着阅读 `code/nano-vllm-hust/nanovllm/engine/block_manager.py` 和 `code/nano-vllm-hust/nanovllm/engine/sequence.py`，整理状态对象与块管理关系图。
5. 最后阅读 `code/nano-vllm-hust/bench.py`，把一次运行整理成结构化实验记录。

## 五、学生练习文件使用方法

`code/nano-vllm-hust/student_exercises/` 中的对应文件并不是让学生机械抄写参考实现，而是要求学生围绕课程问题自行补全关键控制点。

配合作业包时，建议按下面的顺序使用：

1. 先阅读 tutorial 文档，明确本次只回答哪一个系统问题。
2. 再阅读 `experiments/nano-vLLM实验课/` 中对应实验课讲义，确认课堂操作步骤和提交要求。
3. 再看 `code/nano-vllm-hust/assignments/tutorial_<n>_spring-2026/README.md`，确认 starter 文件和提交模板。
4. 完成 `student_exercises/` 中与本次实验对应的 TODO。
5. 把代码改动、日志和解释一起整理回作业包中的报告模板，而不是把代码和结果分开提交。

使用建议：

- 先阅读 `code/nano-vllm-hust/nanovllm/` 中的参考实现。
- 再打开 `code/nano-vllm-hust/student_exercises/` 中对应文件。
- 仅补全与本次 tutorial 问题直接相关的 TODO。
- 在提交报告时，说明你修改的控制点、影响对象和预期系统效果。

如果需要重新生成作业包，可使用 `code/nano-vllm-hust/scripts/teaching/prepare_assignment.py`；如果要汇总 Tutorial 5 的结果，可使用 `code/nano-vllm-hust/scripts/teaching/collect_benchmark_results.py`。

## 六、课程实验任务建议

### 实验一：请求主路径跟踪

- 目标：解释 `add_request()` 到 `generate()` 的完整路径。
- 交付：一张请求生命周期图和一段 500 字左右说明。

### 实验二：调度器行为分析

- 目标：分析 prefill 与 decode 的调度分支，以及抢占出现的条件。
- 交付：调度状态转移图和关键函数说明。

### 实验三：KV block 管理分析

- 目标：解释 block 分配、哈希复用与回收机制。
- 交付：块生命周期图和 `BlockManager` 逻辑总结。

### 实验四：最小 benchmark 复现实验

- 目标：运行 `code/nano-vllm-hust/bench.py` 或其教学变体，记录一次完整实验。
- 交付：环境配置、输入分布、输出结果和结果解释。

## 七、提交要求

每次实验建议至少提交以下内容：

- 实验目标
- 涉及文件与函数
- 核心实现或阅读结论
- 结果截图或运行记录
- 对系统行为的解释

## 八、评分建议

课程实验的评分重点不应只看“是否跑通”，而应同时考察：

- 是否准确定位了控制点
- 是否理解了状态对象与执行路径的关系
- 是否能把运行结果解释为系统现象
- 是否形成了可复查的实验记录

## 九、延伸方向

完成基础实验后，可以继续做以下扩展：

- 在 `code/nano-vllm-hust/bench.py` 基础上增加结构化结果导出
- 对比 `code/nano-vllm-hust/student_exercises/` 与参考实现的行为差异
- 结合课程项目，在 `code/nano-vllm-hust` 上加入新的观测指标或调度策略