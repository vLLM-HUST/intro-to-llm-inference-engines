# nano-vllm-hust Teaching Guide

## Repository Role

`nano-vllm-hust` is a teaching fork of Nano-vLLM prepared for the HUST course on LLM inference infrastructure.

This repository intentionally contains two parallel surfaces:

- `nanovllm/`: the runnable reference implementation kept close to upstream.
- `student_exercises/`: the stripped exercise version where selected functions are replaced with TODOs for students to complete.

## Why keep both surfaces

The experiments need both a reference path and an exercise path, while the tutorials stay focused on theory and question framing.

- Experiment 1 and the early practice-linked sessions need a runnable codebase for code reading and path tracing.
- Experiments 2-5 need carefully chosen missing pieces so students can implement request handling, scheduling, KV state management, and experiment logging themselves.

If we only keep the stripped version, students lose a stable reference.
If we only keep the full version, the practice part becomes too passive.

## Tutorial And Practice Mapping

The full lecture-by-lecture tutorial sequence now lives in the course repository under `src/tutorials/`, where Tutorials 1-13 cover Lectures 2-14 one by one.

This code repository only needs to map the five practice-linked sessions that have matching exercise files or assignment packages.

| Practice-linked tutorial | Related lectures | Tutorial focus | Reference files | Matching practice surface |
| --- | --- | --- | --- | --- |
| 1 | Lecture 2, Lecture 7 | Code map and request entry understanding | `example.py`, `nanovllm/llm.py`, `nanovllm/engine/llm_engine.py` | `src/experiments/nano-vLLM实验课/experiment_1_最小运行与代码地图/assignment_spring-2027/` |
| 2 | Lecture 3 | Lifecycle boundary judgment | `nanovllm/engine/llm_engine.py`, `nanovllm/engine/sequence.py` | `student_exercises/nanovllm/engine/llm_engine.py`, `src/experiments/nano-vLLM实验课/experiment_2_请求生命周期观察/assignment_spring-2027/` |
| 3 | Lecture 4 | Scheduling control-point judgment | `nanovllm/engine/scheduler.py` | `student_exercises/nanovllm/engine/scheduler.py`, `src/experiments/nano-vLLM实验课/experiment_3_调度与连续批处理实验/assignment_spring-2027/` |
| 4 | Lecture 5 | KV organization and cache reasoning | `nanovllm/engine/block_manager.py`, `nanovllm/engine/sequence.py` | `student_exercises/nanovllm/engine/block_manager.py`, `src/experiments/nano-vLLM实验课/experiment_4_KV状态与缓存组织实验/assignment_spring-2027/` |
| 10 | Lecture 11 | Experiment-credibility judgment | `bench.py` | `student_exercises/bench.py`, `src/experiments/nano-vLLM实验课/experiment_5_指标观测与最小复现实验/assignment_spring-2027/` |

The table above intentionally separates the tutorial focus from the matching practice surface. Tutorials are for understanding and judgment; `student_exercises/` and assignment packages are for hands-on practice.

## Closed Teaching Loop

The course materials are intended to be read as one loop instead of treating tutorials and experiments as the same thing.

1. `src/docs/` and `build/slides/` define the system question, boundary, and evaluation language.
2. `build/tutorials/` narrows that question to one concept, one control point judgment, and a small set of must-answer questions.
3. `src/experiments/` turns the same topic into a detailed lab handout with concrete observation, implementation, and submission requirements.
4. `nanovllm/` shows the runnable reference path, while `student_exercises/` exposes the exact control point students must complete in practice.
5. Each `experiment_*` directory and `scripts/teaching/` keep packaging, submission, and result aggregation aligned with the corresponding experiment session.

## Suggested Teaching Workflow

1. Instructors first use `build/tutorials/` to frame the concept and the key question.
2. Instructors then use the reference implementation for walkthroughs.
3. Students enter the matching `src/experiments/` handout and fill the TODOs from `student_exercises/`.
4. Students compare their behavior against the reference implementation when debugging.
5. Course project teams can either continue from the student implementation or instrument the reference implementation.

## TA Workflow

Teaching assistants can use the helper scripts under `scripts/teaching/`.

- `python3 scripts/teaching/prepare_assignment.py 3 --course-tag spring-2027`
	creates a distributable tutorial assignment from `student_exercises/`.
- `python3 scripts/teaching/collect_benchmark_results.py submissions/tutorial5 --output summaries/tutorial5.csv`
	aggregates student benchmark CSV files into one grading table.

These scripts are intended to keep assignment packaging and result collection consistent across the five practice-linked rounds.

## Exercise Boundaries

The stripped files only remove code at the control points that match the course goals:

- request ingestion and engine stepping
- scheduling and postprocess decisions
- KV block allocation and prefix-hash maintenance
- benchmark logging and experiment normalization

The model layers and heavyweight kernel logic are left intact on purpose. The course focus is runtime control and state management, not reimplementing every tensor operator.

## Upstream Relationship

This fork is derived from `GeeeekExplorer/nano-vllm`.
Keep the upstream license file intact.
When syncing future upstream improvements, avoid overwriting the teaching files under `student_exercises/` without review.
