#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
COURSE_ROOT = REPO_ROOT.parents[2]
STUDENT_ROOT = REPO_ROOT / "student_exercises"
EXPERIMENTS_ROOT = COURSE_ROOT / "src" / "experiments" / "nano-vLLM实验课"


@dataclass(frozen=True)
class ExperimentSpec:
    experiment_id: str
    title: str
    folder_name: str
    files: tuple[str, ...]
    question: str


EXPERIMENTS: dict[str, ExperimentSpec] = {
    "1": ExperimentSpec(
        experiment_id="1",
        title="最小运行与代码地图",
        folder_name="experiment_1_最小运行与代码地图",
        files=(),
        question="一次请求从哪里进入系统、经过哪些关键对象、又在哪里返回结果？",
    ),
    "2": ExperimentSpec(
        experiment_id="2",
        title="请求生命周期实践",
        folder_name="experiment_2_请求生命周期观察",
        files=("nanovllm/engine/llm_engine.py",),
        question="如何围绕请求生命周期补全关键控制点，并验证一次请求的执行过程？",
    ),
    "3": ExperimentSpec(
        experiment_id="3",
        title="调度与连续批处理实践",
        folder_name="experiment_3_调度与连续批处理实验",
        files=("nanovllm/engine/scheduler.py",),
        question="如何围绕调度控制点实现或验证 prefill/decode 组织与状态回收逻辑？",
    ),
    "4": ExperimentSpec(
        experiment_id="4",
        title="KV Block 与状态组织",
        folder_name="experiment_4_KV状态与缓存组织实验",
        files=("nanovllm/engine/block_manager.py",),
        question="KV block 如何分配、复用、哈希和释放？",
    ),
    "5": ExperimentSpec(
        experiment_id="5",
        title="Benchmark 与实验记录实践",
        folder_name="experiment_5_指标观测与最小复现实验",
        files=("bench.py",),
        question="如何把 benchmark 运行整理成可复查、可比较的实验记录？",
    ),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create an experiment assignment skeleton from student_exercises.",
    )
    parser.add_argument(
        "experiment",
        choices=sorted(EXPERIMENTS.keys()),
        help="Experiment number to prepare.",
    )
    parser.add_argument(
        "--course-tag",
        default="spring-2027",
        help="Short course tag used in the output directory name.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=EXPERIMENTS_ROOT,
        help="Where experiment source directories live. Defaults to src/experiments/nano-vLLM实验课/.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing assignment directory.",
    )
    return parser


def render_readme(spec: ExperimentSpec) -> str:
    file_list = "\n".join(f"- `{path}`" for path in spec.files)
    starter_section = file_list if file_list else "- 本次作业不直接提供 TODO 源码，重点是代码地图、调用链和日志观测。"
    if spec.files:
        submission_section = (
            "1. Filled source file(s).\n"
            "2. A short report explaining the control point you changed.\n"
            "3. Logs or result tables that support your explanation.\n\n"
        )
    else:
        submission_section = (
            "1. A completed worksheet for the code map and shortest call chain.\n"
            "2. A short report explaining your initial judgment about the first control point.\n"
            "3. Logs, traces, or screenshots that support your walkthrough.\n\n"
        )
    return f"# Experiment {spec.experiment_id} Assignment\n\n" \
        f"## Title\n\n{spec.title}\n\n" \
        f"## Core Question\n\n{spec.question}\n\n" \
        "## Starter Files\n\n" \
        f"{starter_section}\n\n" \
        "## Required Submission\n\n" \
        f"{submission_section}" \
        "## Notes\n\n" \
        "- Do not replace TODOs by copying the reference file mechanically.\n" \
        "- Keep your implementation aligned with the corresponding experimental sheet.\n"


def render_report_template(spec: ExperimentSpec) -> str:
    code_path_prompts = (
        "- Which file and function did you modify?\n"
        "- What system object does this control point own?\n\n"
    )
    implementation_prompt = "Describe the logic you filled in and why it is correct.\n\n"
    if not spec.files:
        code_path_prompts = (
            "- Which file and function did you inspect first?\n"
            "- Which object currently looks like the first control point?\n\n"
        )
        implementation_prompt = "Describe how you reconstructed the request path and why your judgment is plausible.\n\n"
    return f"# Experiment {spec.experiment_id} Report Template\n\n" \
        "## System Question\n\n" \
        f"{spec.question}\n\n" \
        "## Code Path\n\n" \
        f"{code_path_prompts}" \
        "## Implementation Notes\n\n" \
        f"{implementation_prompt}" \
        "## Evidence\n\n" \
        "Paste logs, tables, or screenshots that show your implementation working.\n\n" \
        "## Failure Condition\n\n" \
        "What result would directly falsify your current explanation?\n"


def render_experiment1_worksheet() -> str:
    return (
        "# Experiment 1 Worksheet\n\n"
        "## 1. Code Map\n\n"
        "| System responsibility | File / class / function | Why you think it owns this responsibility |\n"
        "| --- | --- | --- |\n"
        "| Request entry |  |  |\n"
        "| Scheduler / engine loop |  |  |\n"
        "| Model execution |  |  |\n"
        "| State / KV related object |  |  |\n"
        "| Output return |  |  |\n\n"
        "## 2. Shortest Call Chain\n\n"
        "Write a 6-10 step call chain for one request.\n\n"
        "```text\n"
        "main -> ... -> response\n"
        "```\n\n"
        "## 3. Minimal Evidence\n\n"
        "Paste one log snippet, one function trace, or one screenshot that supports your call chain.\n\n"
        "## 4. Initial Judgment\n\n"
        "Where is the first real control point in this runtime? Why?\n"
    )


def prepare_assignment(spec: ExperimentSpec, course_tag: str, output_root: Path, force: bool) -> Path:
    experiment_dir = output_root / spec.folder_name
    assignment_dir = experiment_dir / f"assignment_{course_tag}"
    starter_dir = assignment_dir / "starter"
    submission_dir = assignment_dir / "submission_template"

    if assignment_dir.exists():
        if not force:
            raise FileExistsError(
                f"Assignment directory already exists: {assignment_dir}. Use --force to overwrite."
            )
        shutil.rmtree(assignment_dir)

    experiment_dir.mkdir(parents=True, exist_ok=True)
    starter_dir.mkdir(parents=True, exist_ok=True)
    submission_dir.mkdir(parents=True, exist_ok=True)

    for relative_path in spec.files:
        source = STUDENT_ROOT / relative_path
        destination = starter_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    (assignment_dir / "README.md").write_text(render_readme(spec), encoding="utf-8")
    (submission_dir / "report_template.md").write_text(
        render_report_template(spec), encoding="utf-8"
    )

    if spec.experiment_id == "1":
        (submission_dir / "worksheet.md").write_text(
            render_experiment1_worksheet(), encoding="utf-8"
        )

    if spec.experiment_id == "5":
        (submission_dir / "results").mkdir(parents=True, exist_ok=True)

    return assignment_dir


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    spec = EXPERIMENTS[args.experiment]
    assignment_dir = prepare_assignment(spec, args.course_tag, args.output_root, args.force)
    print(f"Created assignment at: {assignment_dir}")


if __name__ == "__main__":
    main()
