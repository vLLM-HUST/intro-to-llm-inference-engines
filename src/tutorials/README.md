# 大模型推理基础设施 Tutorials 总览

`src/tutorials/` 只放 tutorial 源材料，不混入实验说明。Markdown 源文件统一放在 `md/`，正式导出的 PDF 统一输出到仓库根目录下的 `build/tutorials/`。

从第 2 讲到第 14 讲共 13 份 tutorial，每讲一份。每份 tutorial 统一采用“混合题型题单 + 参考答案”结构，合计约 10 题，题目和答案分页呈现。题型会混合单选、多选、判断、简答、计算和伪代码等形式。题目要求比 lecture 稍深一层，强调边界判断、迁移判断和反例判断，不重复讲义原句。

Tutorial 和 experiment 的分工很明确：tutorial 用于检查学生是否真正理解课堂内容，experiment 用于动手运行、插桩、记录和提交。代码操作、日志、参数修改和实验步骤统一放在 `src/experiments/`。

如需重新生成 PDF，请在 `src/tutorials/` 目录执行 `make`，或在仓库根目录执行 `make tutorials`。

## 对应关系

1. `md/Tutorial_01_工作负载与评价指标.md` 对应第 2 讲。
2. `md/Tutorial_02_请求生命周期与PrefillDecode.md` 对应第 3 讲。
3. `md/Tutorial_03_调度与连续批处理观察.md` 对应第 4 讲。
4. `md/Tutorial_04_KV_Cache与状态组织.md` 对应第 5 讲。
5. `md/Tutorial_05_状态管理与记忆组织.md` 对应第 6 讲。
6. `md/Tutorial_06_推理系统架构.md` 对应第 7 讲。
7. `md/Tutorial_07_执行优化与异构路径.md` 对应第 8 讲。
8. `md/Tutorial_08_异构平台适配.md` 对应第 9 讲。
9. `md/Tutorial_09_论文比较方法.md` 对应第 10 讲。
10. `md/Tutorial_10_实验方法与验证.md` 对应第 11 讲。
11. `md/Tutorial_11_开源系统实践.md` 对应第 12 讲。
12. `md/Tutorial_12_课程项目工作坊.md` 对应第 13 讲。
13. `md/Tutorial_13_课程总结与汇报.md` 对应第 14 讲。
