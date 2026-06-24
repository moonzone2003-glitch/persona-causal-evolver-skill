#!/usr/bin/env python3
"""Append a self-growth training log entry as JSONL."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Append self-growth training log")
    parser.add_argument("--log", required=True, help="JSONL log path")
    parser.add_argument("--domain", required=True)
    parser.add_argument(
        "--mode",
        required=True,
        choices=[
            "daily_review",
            "targeted_training",
            "future_self",
            "monthly_evolution",
            "knowledge_internalization",
            "expert_contrast",
            "internalization_verification",
        ],
    )
    parser.add_argument("--score", type=float)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--tasks", default="[]", help="JSON array of training tasks")
    args = parser.parse_args()

    log_path = Path(args.log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    tasks = json.loads(args.tasks)
    entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "domain": args.domain,
        "mode": args.mode,
        "score": args.score,
        "summary": args.summary,
        "tasks": tasks,
    }
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "ok", "log": str(log_path), "entry": entry}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
