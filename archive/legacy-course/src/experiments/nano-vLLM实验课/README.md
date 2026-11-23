# nano-vLLM 实验材料说明

## 定位

本目录承接《大模型推理系统与实践》课程的实验课部分。这里的材料按实验单的方式组织：文档直接面向学生，能够独立支撑一次完整实验，不依赖教师口头补充才能完成。

每份实验单原则上都应包含以下模块：

1. 对应 lecture / tutorial 与本节核心问题。
2. 学习目标与先修要求。
3. 环境、代码入口与材料清单。
4. 分步实验任务与过程记录模板。
5. 明确的证据要求与提交内容。
6. 提交清单与评分关注点。

## 与 tutorials 的分工

- `src/tutorials/`：用于课堂理解练习，重点是概念辨析、推理链条和边界判断。
- `src/experiments/`：用于动手训练，重点是运行、插桩、观测、记录、复核和提交。

两者必须严格区分。tutorial 不替代实验，experiment 也不重复 tutorial 的问答题单。

## 目录组织

本目录现在按实验分组组织，而不是按“实验单 / 作业包 / PDF”三类材料分开组织。

1. `experiment_1_最小运行与代码地图/`
	- `sheet.md`
	- `assignment_spring-2027/`
	- `archive/`
2. `experiment_2_请求生命周期观察/`
	- `sheet.md`
	- `assignment_spring-2027/`
3. `experiment_3_调度与连续批处理实验/`
	- `sheet.md`
	- `assignment_spring-2027/`
4. `experiment_4_KV状态与缓存组织实验/`
	- `sheet.md`
	- `assignment_spring-2027/`
5. `experiment_5_指标观测与最小复现实验/`
	- `sheet.md`
	- `assignment_spring-2027/`
正式发放版 PDF 不再与源码混放，而是统一输出到仓库根目录下的 `build/experiments/nano-vLLM实验课/`。

课程考核使用 [vLLM-HUST MOD 个人项目实验单](../../../build/experiments/mod-project/vLLM-HUST_MOD_个人项目实验单.pdf)。

## 建议使用顺序

1. 先用 `build/slides/` 与 `src/docs/` 讲清本周系统问题。
2. 再用 `build/tutorials/` 收束概念、边界和推理链。
3. 最后发放本目录实验单，让学生围绕真实代码完成运行、观测和记录。

## 当前整理原则

- 文风以学生使用为主，不写成教师讲稿。
- 任务设计强调可操作、可复核、可提交。
- 每份实验都应要求学生提供最小证据，而不是只交结论。
- 不发明额外课程政策、截止时间或分值；若课程安排未定，只写提交内容与评分关注点。

## PDF 导出

本目录支持直接导出正式发放版 PDF：

1. 在本目录运行 `make`，会为五份实验单生成对应的 PDF。
2. 导出的 PDF 统一放在仓库根目录下的 `build/experiments/nano-vLLM实验课/`，便于集中发放与同步到 public-site。
3. 如需清理导出文件，可运行 `make clean`。

当前默认导出实验一到实验五。

## 目录结构

- 根目录：`README.md`、`Makefile`、`pandoc/` 与各个实验源目录。
- 各个 `experiment_*` 目录：`sheet.md` 与对应 `assignment_spring-2027/`。
- 正式 PDF：统一输出到 `build/experiments/nano-vLLM实验课/`。
