# nano-vllm-hust 课程作业说明

## 一、说明

本说明面向“大模型推理基础设施”课程的学生与助教，配合 `nano-vllm-hust` 教学代码库使用。

课程实践部分现在采用“tutorial 理论导学 + experiment 实验课 + assignment 作业包”三层组织。作业包继续沿用 tutorial 编号，但详细课堂实验流程已迁移到 `experiments/nano-vLLM实验课/`。

## 二、作业目录

本轮课程作业包已生成在以下目录中：

- `code/nano-vllm-hust/assignments/tutorial_1_spring-2026`
- `code/nano-vllm-hust/assignments/tutorial_2_spring-2026`
- `code/nano-vllm-hust/assignments/tutorial_3_spring-2026`
- `code/nano-vllm-hust/assignments/tutorial_4_spring-2026`
- `code/nano-vllm-hust/assignments/tutorial_5_spring-2026`

每个作业目录通常包含：

- `README.md`：本次作业的标题、核心问题和提交要求。
- `starter/`：从 `code/nano-vllm-hust/student_exercises/` 复制出的教学起始文件。
- `submission_template/`：报告模板、worksheet 或结果目录模板。

## 三、五次 tutorial 的课程映射

### Tutorial 1：最小运行与代码地图

- 课程主题：请求生命周期与系统入口
- 核心问题：一次请求从哪里进入系统、经过哪些关键对象、又在哪里返回结果？
- 主要交付：代码地图、最短调用链、初始控制点判断

### Tutorial 2：请求生命周期与 Engine Step

- 课程主题：请求注入与单步执行
- 核心问题：一次请求如何进入系统、完成一步执行并返回结果？
- 主要交付：`llm_engine.py` 中相关 TODO 的实现与解释

### Tutorial 3：调度与 Postprocess

- 课程主题：prefill/decode 调度与状态回收
- 核心问题：调度器如何决定 prefill/decode，并在结束时回收状态？
- 主要交付：`scheduler.py` 中调度控制点的实现与说明

### Tutorial 4：KV Block 与状态组织

- 课程主题：KV block 分配、复用与哈希
- 核心问题：KV block 如何分配、复用、哈希和释放？
- 主要交付：`block_manager.py` 中状态管理逻辑的实现与说明

### Tutorial 5：实验记录与 Benchmark 结果

- 课程主题：benchmark 运行与结构化结果整理
- 核心问题：如何把运行记录整理成可复现实验结果？
- 主要交付：`code/nano-vllm-hust/bench.py` 相关实现、benchmark 结果和结构化实验记录

## 四、学生提交要求

每次 tutorial 至少提交以下内容：

- 修改后的 starter 文件或 worksheet
- 一份简短实验/实现报告
- 支撑结论的日志、截图、结果表或 trace

建议报告统一回答以下问题：

- 你修改或观察了哪个控制点？
- 该控制点管理的系统对象是什么？
- 你的证据支持什么结论？
- 什么结果会直接否定你的当前解释？

## 五、建议教学节奏

建议按以下节奏组织 tutorial：

1. 课堂上先用 tutorial 讲清本次系统问题。
2. 再进入 `experiments/nano-vLLM实验课/` 中对应实验课讲义。
3. 然后用 `code/nano-vllm-hust/nanovllm/` 中的参考实现进行最小源码导读。
4. 最后布置 `code/nano-vllm-hust/student_exercises/` 中对应的 TODO 作业与结构化报告。

## 六、助教工作流

助教可直接使用仓库内脚本维持作业分发与结果汇总的一致性。

### 1. 生成作业包

```bash
cd code/nano-vllm-hust
python3 scripts/teaching/prepare_assignment.py 3 --course-tag spring-2026 --force
```

### 2. 汇总 benchmark 结果

```bash
cd code/nano-vllm-hust
python3 scripts/teaching/collect_benchmark_results.py submissions/tutorial5 --output summaries/tutorial5.csv
```

`collect_benchmark_results.py` 会递归查找学生提交目录中的 benchmark CSV，并生成按学生汇总的总表。

## 七、评分建议

评分时建议同时考察以下维度：

- 是否找对了控制点
- 是否解释了状态对象与执行行为的关系
- 是否给出了足以支撑结论的证据
- 是否形成了可复查、可比较的实验记录

## 八、与课程项目的衔接

Tutorial 不应被看作孤立作业，而应作为课程项目的准备阶段。

- Tutorial 1 到 3 训练请求路径和调度控制能力。
- Tutorial 4 训练状态对象与 KV 管理能力。
- Tutorial 5 训练实验设计与结果整理能力。

完成全部 tutorial 后，学生应具备进入课程项目的最小代码与实验基础。