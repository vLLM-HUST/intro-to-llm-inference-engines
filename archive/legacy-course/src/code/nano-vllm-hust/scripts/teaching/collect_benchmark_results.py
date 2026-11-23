#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


DEFAULT_PATTERN = "tutorial5_benchmark.csv"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect benchmark CSV files from student submissions into one summary table.",
    )
    parser.add_argument(
        "submissions_root",
        type=Path,
        help="Root directory containing student submission folders.",
    )
    parser.add_argument(
        "--pattern",
        default=DEFAULT_PATTERN,
        help="Benchmark CSV filename to search for.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("collected_benchmark_results.csv"),
        help="Path of the aggregated CSV to write.",
    )
    return parser


def infer_student_name(csv_path: Path, submissions_root: Path) -> str:
    parent = csv_path.parent
    if parent.name == "results":
        parent = parent.parent
    try:
        relative = parent.relative_to(submissions_root)
        return relative.parts[0]
    except ValueError:
        return parent.name


def collect_rows(submissions_root: Path, pattern: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for csv_path in sorted(submissions_root.rglob(pattern)):
        student = infer_student_name(csv_path, submissions_root)
        with csv_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                merged = {"student": student, "source_file": str(csv_path.relative_to(submissions_root))}
                merged.update(row)
                rows.append(merged)
    return rows


def write_rows(output_path: Path, rows: list[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        output_path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict[str, str]]) -> None:
    if not rows:
        print("No benchmark rows found.")
        return
    grouped: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        throughput = row.get("throughput")
        if throughput:
            grouped[row["student"]].append(float(throughput))

    print("Collected benchmark rows:")
    print(f"- total rows: {len(rows)}")
    print(f"- students: {len(grouped)}")
    for student, values in sorted(grouped.items()):
        avg = sum(values) / len(values)
        print(f"- {student}: {len(values)} run(s), avg throughput={avg:.4f}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    rows = collect_rows(args.submissions_root, args.pattern)
    write_rows(args.output, rows)
    print_summary(rows)
    print(f"Wrote aggregated CSV to: {args.output}")


if __name__ == "__main__":
    main()
