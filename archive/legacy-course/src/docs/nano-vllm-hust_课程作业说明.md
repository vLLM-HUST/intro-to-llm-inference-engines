# nano-vllm-hust 课程作业说明

## 一、说明

本说明面向《大模型推理系统与实践》课程的学生与助教，配合 `nano-vllm-hust` 教学代码库使用。

课程实践采用 tutorial 理解练习、experiment 实验课和 assignment 作业包三层组织。Tutorial 对应十四讲细分课件的第 2–14 讲，共 13 份。实验和作业包提供 5 个实践任务，用于训练系统观测和复现。2027 年课程总评全部来自 [MOD 项目](../site/tutorials/assessment/index.html)。

## 二、作业目录

本轮课程作业包已生成在以下目录中：

- `src/experiments/nano-vLLM实验课/experiment_1_最小运行与代码地图/assignment_spring-2027`
- `src/experiments/nano-vLLM实验课/experiment_2_请求生命周期观察/assignment_spring-2027`
- `src/experiments/nano-vLLM实验课/experiment_3_调度与连续批处理实验/assignment_spring-2027`
- `src/experiments/nano-vLLM实验课/experiment_4_KV状态与缓存组织实验/assignment_spring-2027`
- `src/experiments/nano-vLLM实验课/experiment_5_指标观测与最小复现实验/assignment_spring-2027`

每个作业目录通常包含：

- `README.md`：本次作业的标题、核心问题和提交要求。
- `starter/`：从 `src/code/nano-vllm-hust/student_exercises/` 复制出的教学起始文件。
- `submission_template/`：报告模板、worksheet 或结果目录模板。

## 三、Tutorial 序列与实践包分工

下表中的 tutorial 主题只描述课堂理解练习的内容，不等同于实验实现任务。涉及 `student_exercises/`、TODO、benchmark 运行和结果提交的内容，统一属于 experiment 与 assignment 层。

| Tutorial | 对应讲次 | 主题 |
| --- | --- | --- |
| Tutorial 1 | 第 2 讲 | 工作负载与评价指标 |
| Tutorial 2 | 第 3 讲 | 请求生命周期与阶段边界 |
| Tutorial 3 | 第 4 讲 | 调度与控制点判断 |
| Tutorial 4 | 第 5 讲 | KV Cache 管理 |
| Tutorial 5 | 第 6 讲 | 状态管理与记忆组织 |
| Tutorial 6 | 第 7 讲 | 推理系统架构 |
| Tutorial 7 | 第 8 讲 | 执行优化与异构路径 |
| Tutorial 8 | 第 9 讲 | 异构平台与国产算力适配 |
| Tutorial 9 | 第 10 讲 | 论文比较方法 |
| Tutorial 10 | 第 11 讲 | 实验方法与验证 |
| Tutorial 11 | 第 12 讲 | 开源系统实践 |
| Tutorial 12 | 第 13 讲 | 课程项目工作坊 |
| Tutorial 13 | 第 14 讲 | 课程总结与汇报 |

与之对应的 experiment / assignment 仍保留 5 个实践包，分别承接第 2、3、4、5、11 讲中动手要求最强的部分。

## 四、学生提交要求

assignment 作业包服务于 experiment 层，而不是 tutorial 层。需要提交代码、日志、截图、结果表或 trace 的内容，均应通过 assignment 包完成。

如果教师仅布置 tutorial 理解练习，建议学生提交以下内容：

- worksheet 或课堂练习答题结果
- 概念图、因果链、职责表等理解性材料
- 简短文字说明

如果教师布置 experiment / assignment 实战任务，则至少提交以下内容：

- 修改后的 starter 文件或 worksheet
- 一份简短实践报告
- 支撑结论的日志、截图、结果表或 trace

建议报告统一回答以下问题：

- 你修改或观察了哪个控制点？
- 该控制点管理的系统对象是什么？
- 你的证据支持什么结论？
- 什么结果会直接否定你的当前解释？

## 五、建议教学节奏

建议按以下节奏组织实践部分：

1. 课堂上先用 tutorial 讲清本次系统问题。
2. 再发放 `build/experiments/nano-vLLM实验课/` 中对应实验课讲义 PDF。
3. 然后用 `src/code/nano-vllm-hust/nanovllm/` 中的参考实现进行最小源码导读。
4. 最后布置 `src/code/nano-vllm-hust/student_exercises/` 中对应的 TODO 作业与结构化报告。

## 六、助教工作流

助教可直接使用仓库内脚本维持作业分发与结果汇总的一致性。

### 1. 生成作业包

```bash
cd src/code/nano-vllm-hust
python3 scripts/teaching/prepare_assignment.py 3 --course-tag spring-2027 --force
```

默认输出目录为各个 experiment 目录下的 `assignment_<course-tag>/`。

### 2. 汇总 benchmark 结果

```bash
cd src/code/nano-vllm-hust
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

Tutorial 与 experiment 都不应被看作孤立任务，而应分别承担“理解准备”和“动手准备”的职责。

- Tutorial 1 到 5 负责建立 workload 指标判断、请求路径、生命周期、调度、KV 与状态管理的理解能力。
- Tutorial 6 到 10 负责建立架构判断、执行优化、平台适配、论文比较与实验方法能力。
- Tutorial 11 到 13 负责把开源系统实践、课程项目和最终汇报收束为完整研究训练过程。

- Experiments 1 到 4 负责训练运行、插桩、观察与代码实现能力。
- Experiment 5 负责训练实验组织、结果整理与报告提交能力。

完成 tutorial 与 experiment 两层后，学生才具备进入课程项目的最小理解基础与动手基础。
