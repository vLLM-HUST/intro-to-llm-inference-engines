# Student Exercises

This directory contains the stripped teaching version of selected Nano-vLLM files.

## How to use

- Read the runnable reference implementation under `nanovllm/` first.
- Then open the matching file under `student_exercises/`.
- Fill the TODO sections.
- Explain the control point you changed and how you expect it to affect system behavior.

## Files

- `nanovllm/engine/llm_engine.py`
  Focus: request ingestion and one engine step.
- `nanovllm/engine/scheduler.py`
  Focus: prefill/decode scheduling and postprocess.
- `nanovllm/engine/block_manager.py`
  Focus: block reuse, allocation, deallocation, and prefix hashing.
- `bench.py`
  Focus: experiment normalization and structured result recording.

## Rule

Do not fill TODOs by blindly copying the reference file.
Each TODO is attached to one tutorial question and one system object. Your implementation should match the tutorial report you submit.
