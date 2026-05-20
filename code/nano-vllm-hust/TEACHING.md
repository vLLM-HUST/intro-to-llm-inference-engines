# nano-vllm-hust Teaching Guide

## Repository Role

`nano-vllm-hust` is a teaching fork of Nano-vLLM prepared for the HUST course on LLM inference infrastructure.

This repository intentionally contains two parallel surfaces:

- `nanovllm/`: the runnable reference implementation kept close to upstream.
- `student_exercises/`: the stripped exercise version where selected functions are replaced with TODOs for students to complete.

## Why keep both surfaces

The experiments need both a reference path and an exercise path, while the tutorials stay focused on theory and question framing.

- Tutorial 1 needs a runnable codebase for code reading and path tracing.
- Experiments 2-5 need carefully chosen missing pieces so students can implement request handling, scheduling, KV state management, and experiment logging themselves.

If we only keep the stripped version, students lose a stable reference.
If we only keep the full version, the practice part becomes too passive.

## Tutorial Mapping

| Tutorial | Related lectures | Reference files | Student exercise files | Assignment package | Main question |
| --- | --- | --- | --- | --- | --- |
| 1 | Lecture 1-2, Lecture 7 | `example.py`, `nanovllm/llm.py`, `nanovllm/engine/llm_engine.py` | none required | `assignments/tutorial_1_spring-2026/` | Where does one request enter and finish? |
| 2 | Lecture 3 | `nanovllm/engine/llm_engine.py`, `nanovllm/engine/sequence.py` | `student_exercises/nanovllm/engine/llm_engine.py` | `assignments/tutorial_2_spring-2026/` | How do add_request and step organize request lifecycle? |
| 3 | Lecture 4 | `nanovllm/engine/scheduler.py` | `student_exercises/nanovllm/engine/scheduler.py` | `assignments/tutorial_3_spring-2026/` | How does scheduling decide who runs next? |
| 4 | Lecture 5-6 | `nanovllm/engine/block_manager.py`, `nanovllm/engine/sequence.py` | `student_exercises/nanovllm/engine/block_manager.py` | `assignments/tutorial_4_spring-2026/` | How is KV state allocated, reused, and hashed? |
| 5 | Lecture 11 | `bench.py` | `student_exercises/bench.py` | `assignments/tutorial_5_spring-2026/` | How do we turn runs into reproducible experiment records? |

## Closed Teaching Loop

The course materials are intended to be read as one loop instead of treating tutorials and experiments as the same thing.

1. `docs/` and `slides/` define the system question, boundary, and evaluation language.
2. `tutorials/` narrows that question to one concept, one control point judgment, and a small set of must-answer questions.
3. `experiments/` turns the same topic into a detailed lab handout with concrete observation and submission requirements.
4. `nanovllm/` shows the runnable reference path, while `student_exercises/` exposes the exact control point students must complete.
5. `assignments/` and `scripts/teaching/` keep packaging, submission, and result aggregation aligned with the corresponding experiment session.

## Suggested Teaching Workflow

1. Instructors first use `tutorials/` to frame the concept and the key question.
2. Instructors then use the reference implementation for walkthroughs.
3. Students enter the matching `experiments/` handout and fill the TODOs from `student_exercises/`.
4. Students compare their behavior against the reference implementation when debugging.
5. Course project teams can either continue from the student implementation or instrument the reference implementation.

## TA Workflow

Teaching assistants can use the helper scripts under `scripts/teaching/`.

- `python3 scripts/teaching/prepare_assignment.py 3 --course-tag 2026-spring`
	creates a distributable tutorial assignment from `student_exercises/`.
- `python3 scripts/teaching/collect_benchmark_results.py submissions/tutorial5 --output summaries/tutorial5.csv`
	aggregates student benchmark CSV files into one grading table.

These scripts are intended to keep assignment packaging and result collection consistent across tutorial rounds.

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
