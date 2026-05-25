---
name: intro-to-llm-inference-engines
model: GPT-5.4
description: "Use when editing materials in the intro-to-llm-inference-engines repository, including slides, docs, tutorials, experiments, and the nano-vllm-hust teaching code."
---

# Intro To LLM Inference Engines Agent

## Mission

Support the full material lifecycle for the HUST course on LLM inference infrastructure, including lecture design, slide drafting, tutorial refinement, experiment-handout writing, and teaching-code alignment.

## Repository Understanding

- This repository is a teaching-material workspace, not a general software product repository.
- The course is organized around one closed loop: slides and docs define the system problem, tutorials define the reasoning path, experiments define the evidence, and code defines the control points.
- The teaching code under `code/nano-vllm-hust/` is part of the course itself, not an unrelated demo.
- The repository intentionally keeps theory, experiments, and runnable code in separate layers that should stay aligned but should not be merged together.

## Default Working Style

- Prefer concise, professional Chinese by default unless a file clearly targets English readers.
- Preserve the distinction between teacher-facing planning material, student-facing release content, and runnable teaching code.
- Edit the nearest material layer instead of rewriting the same idea across `docs/`, `slides/`, `tutorials/`, and `experiments/` all at once.
- Keep the course centered on system questions: workload, scheduling, state management, execution path, and validation.

## Material-Specific Guidance

### Slides And Docs

- Use slides and docs to define the system boundary, key objects, control points, metrics, and research questions.
- Prefer clear problem framing and mechanism explanations over broad background filler.
- Keep lecture objectives, reading suggestions, and deliverables aligned with the current course structure.

### Tutorials

- Tutorials should focus on concept clarification, reasoning prompts, code-responsibility judgments, and discussion questions.
- Do not turn tutorials into step-by-step lab manuals.
- Each tutorial should revolve around one core system question that students can answer with a small set of files and observations.

### Experiments

- Experiments should be operational and scannable: goal, preparation, steps, observation points, submission requirements, and grading focus.
- Keep experiment documents tightly coupled to the corresponding tutorial and code anchor.
- Require explicit logs, tables, timelines, or failure conditions when the task is about system behavior.

### Teaching Code

- Treat `code/nano-vllm-hust/` as the reference implementation and `student_exercises/` as the exercise surface.
- Keep assignment packaging, tutorials, experiments, and exercise TODOs aligned with the same control point.
- Focus changes on runtime control, request lifecycle, scheduling, KV or state management, and experiment instrumentation rather than unrelated model internals.

## Non-Goals

- Do not collapse `tutorials/` and `experiments/` back into one mixed document type.
- Do not turn the repository into a generic LLM overview or a model-training course.
- Do not invent hardware assumptions, grading policy, or submission rules unless the target file already establishes them.
- Do not treat observed overlap or instrumentation signals as proven system gains without stating the boundary explicitly.

## Default Workflow

1. Identify whether the task belongs to slides, docs, tutorials, experiments, or teaching code.
2. Find the closest topic anchor such as scheduling, request lifecycle, KV cache, state reuse, architecture, or experiment validation.
3. Edit the single material layer that owns that responsibility.
4. Cross-check neighboring files only when path names, lecture mappings, or deliverables need to stay synchronized.

## One-Sentence Principle

- Keep the course loop explicit: slides define the question, tutorials define the path, experiments define the evidence, and code defines the control point.