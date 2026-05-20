# Tutorial 2：请求生命周期与 Prefill/Decode

## 本次联动位置

- 对应讲次：第 3 讲“一次推理请求的完整生命周期”。
- 对应实验：`experiments/nano-vLLM实验课/实验二_请求生命周期观察.md`。
- 参考代码：`code/nano-vllm-hust/nanovllm/engine/llm_engine.py`、`code/nano-vllm-hust/nanovllm/engine/sequence.py`。
- 本 tutorial 负责阶段辨析与概念问答，不负责具体插桩步骤。

## 目标

本 tutorial 把“请求生命周期”从课堂概念变成系统判断。学生完成后应能回答：

- 一次请求在系统里经历了哪些阶段。
- prefill 和 decode 在代码组织、时间分布和资源特征上有什么差异。

## 本 tutorial 不做什么

- 不提供实验命令和日志模板。
- 不要求学生在此文档中直接提交时序图。
- 不要求在本节 tutorial 中实现代码 TODO。

## 核心概念

- 生命周期不是自然语言阶段名堆砌，而是控制权和状态变化的组织方式。
- prefill 和 decode 不只是“前半段/后半段”，而是两类资源特征不同的阶段。
- 若不区分阶段，TTFT、queue wait 和后续调度分析都容易被写混。

## 必答问题

1. 为什么长 prompt 往往先放大 prefill 代价。
2. decode 为什么更容易与调度、并发和 KV 驻留绑定在一起。
3. 如果把 prefill 和 decode 混成一种任务，最可能误读哪些指标。

## 课堂追问

- 生命周期图里最重要的不是“阶段多”，而是“阶段边界准”，你同意吗。
- 如果某个系统文档没有明确写 prefill/decode，但代码里存在这种分化，学生该如何判断。
- TTFT 这个指标为什么天然更贴近 prefill 与排队，而不是完整 decode 过程。

## 推荐阅读与观察

- `code/nano-vllm-hust/nanovllm/engine/llm_engine.py`
- `code/nano-vllm-hust/nanovllm/engine/sequence.py`

观察重点：

- 哪些函数更像阶段边界。
- 哪些对象跨阶段持续存在。
- 哪些指标与哪个阶段天然更强相关。

## 推荐产出

- 一张生命周期概念图。
- 一段 400-600 字说明：你如何区分 prefill 和 decode，以及这种区分对指标解释有什么意义。

## 本 tutorial 应回答的问题

- 为什么阶段划分本身就是系统判断，而不是文书整理。
- 为什么 lifecycle tutorial 必须在调度和 KV tutorial 之前。
- 为什么阶段视角会影响你如何读 benchmark 结果。
