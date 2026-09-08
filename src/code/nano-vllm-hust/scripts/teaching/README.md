# Teaching Scripts

## Overview

These scripts are for teaching assistants and instructors using `nano-vllm-hust` in class.

## Scripts

### `prepare_assignment.py`

Create an experiment-specific assignment skeleton from `student_exercises/`.

Example:

```bash
python3 scripts/teaching/prepare_assignment.py 3 --course-tag spring-2027
```

This creates:

- `../../../../experiments/nano-vLLM实验课/experiment_3_调度与连续批处理实验/assignment_spring-2027/starter/`
- `../../../../experiments/nano-vLLM实验课/experiment_3_调度与连续批处理实验/assignment_spring-2027/submission_template/`
- an experiment-specific `README.md`

### `collect_benchmark_results.py`

Aggregate student benchmark CSV files into one table.

Example:

```bash
python3 scripts/teaching/collect_benchmark_results.py submissions/tutorial5 --output summaries/tutorial5.csv
```

The script searches recursively for `tutorial5_benchmark.csv`, adds the inferred student name, writes an aggregated CSV, and prints a small throughput summary.

## Recommended Workflow

1. Use `prepare_assignment.py` to generate the starter package for an experiment.
2. The generated package is placed inside the matching experiment source directory under `src/experiments/nano-vLLM实验课/`, not inside the code tree.
2. Distribute the generated `starter/` directory to students.
3. Ask students to keep benchmark outputs under a `results/` directory.
4. Use `collect_benchmark_results.py` after submission deadline to gather all CSV files.
