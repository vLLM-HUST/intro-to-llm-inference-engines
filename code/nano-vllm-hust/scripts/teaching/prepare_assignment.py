#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
STUDENT_ROOT = REPO_ROOT / "student_exercises"
ASSIGNMENTS_ROOT = REPO_ROOT / "assignments"


@dataclass(frozen=True)
class TutorialSpec:
    tutorial_id: str
    title: str
    files: tuple[str, ...]
    question: str


TUTORIALS: dict[str, TutorialSpec] = {
    "1": TutorialSpec(
        tutorial_id="1",
        title="最小运行与代码地图",
        files=(),
        question="一次请求从哪里进入系统、经过哪些关键对象、又在哪里返回结果？",
    ),
    "2": TutorialSpec(
        tutorial_id="2",
        title="请求生命周期与 Engine Step",
        files=("nanovllm/engine/llm_engine.py",),
        question="一次请求如何进入系统、完成一步执行并返回结果？",
    ),
    "3": TutorialSpec(
        tutorial_id="3",
        title="调度与 Postprocess",
        files=("nanovllm/engine/scheduler.py",),
        question="调度器如何决定 prefill/decode，并在结束时回收状态？",
    ),
    "4": TutorialSpec(
        tutorial_id="4",
        title="KV Block 与状态组织",
        files=("nanovllm/engine/block_manager.py",),
        question="KV block 如何分配、复用、哈希和释放？",
    ),
    "5": TutorialSpec(
        tutorial_id="5",
        title="实验记录与 Benchmark 结果",
        files=("bench.py",),
        question="如何把运行记录整理成可复现实验结果？",
    ),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a tutorial assignment skeleton from student_exercises.",
    )
    parser.add_argument(
        "tutorial",
        choices=sorted(TUTORIALS.keys()),
        help="Tutorial number to prepare.",
    )
    parser.add_argument(
        "--course-tag",
        default="spring-2026",
        help="Short course tag used in the output directory name.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=ASSIGNMENTS_ROOT,
        help="Where generated assignment folders should be created.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing assignment directory.",
    )
    return parser


def render_readme(spec: TutorialSpec) -> str:
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
    return f"# Tutorial {spec.tutorial_id} Assignment\n\n" \
        f"## Title\n\n{spec.title}\n\n" \
        f"## Core Question\n\n{spec.question}\n\n" \
        "## Starter Files\n\n" \
        f"{starter_section}\n\n" \
        "## Required Submission\n\n" \
        f"{submission_section}" \
        "## Notes\n\n" \
        "- Do not replace TODOs by copying the reference file mechanically.\n" \
        "- Keep your implementation aligned with the corresponding tutorial report.\n"


def render_report_template(spec: TutorialSpec) -> str:
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
    return f"# Tutorial {spec.tutorial_id} Report Template\n\n" \
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


def render_tutorial1_worksheet() -> str:
    return (
        "# Tutorial 1 Worksheet\n\n"
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


def prepare_assignment(spec: TutorialSpec, course_tag: str, output_root: Path, force: bool) -> Path:
    assignment_dir = output_root / f"tutorial_{spec.tutorial_id}_{course_tag}"
    starter_dir = assignment_dir / "starter"
    submission_dir = assignment_dir / "submission_template"

    if assignment_dir.exists():
        if not force:
            raise FileExistsError(
                f"Assignment directory already exists: {assignment_dir}. Use --force to overwrite."
            )
        shutil.rmtree(assignment_dir)

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

    if spec.tutorial_id == "1":
        (submission_dir / "worksheet.md").write_text(
            render_tutorial1_worksheet(), encoding="utf-8"
        )

    if spec.tutorial_id == "5":
        (submission_dir / "results").mkdir(parents=True, exist_ok=True)

    return assignment_dir


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    spec = TUTORIALS[args.tutorial]
    assignment_dir = prepare_assignment(spec, args.course_tag, args.output_root, args.force)
    print(f"Created assignment at: {assignment_dir}")


if __name__ == "__main__":
    main()
