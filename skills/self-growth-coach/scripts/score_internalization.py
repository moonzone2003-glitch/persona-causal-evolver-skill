#!/usr/bin/env python3
"""Score whether a training result is actually internalized.

Input JSON schema:
{
  "domain": "ai_coding",
  "scores": {
    "理解": 7,
    "迁移": 6,
    "决策改善": 6,
    "执行": 4,
    "保持": 2
  },
  "evidence_count": 3,
  "real_world_execution_count": 1,
  "delayed_review_days": 0,
  "confidence": "medium"
}
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

WEIGHTS = {
    "理解": 1.0,
    "迁移": 1.2,
    "决策改善": 1.3,
    "执行": 1.4,
    "保持": 1.1,
}


def clamp_score(value: object) -> float:
    return max(0.0, min(10.0, float(value)))


def weighted_score(scores: dict[str, object]) -> float:
    weighted = 0.0
    total_weight = 0.0
    for key, value in scores.items():
        weight = WEIGHTS.get(key, 1.0)
        weighted += clamp_score(value) * weight
        total_weight += weight
    return round(weighted / total_weight, 2) if total_weight else 0.0


def classify(score: float, execution_count: int, delayed_days: int) -> tuple[str, str]:
    if execution_count <= 0:
        return "candidate_only", "只有模型输出或计划，没有现实执行证据"
    if score < 5:
        return "not_internalized", "内化分低，继续训练，不回流人格"
    if score < 7:
        return "partial_internalization", "已有部分内化证据，继续观察"
    if delayed_days < 7:
        return "needs_delayed_review", "分数较高但缺少延迟保持证据"
    return "evolver_review_ready", "可交给 persona-causal-evolver 判断是否稳定回灌"


def main() -> None:
    parser = argparse.ArgumentParser(description="Score internalization from training JSON")
    parser.add_argument("--input", required=True, help="Path to internalization JSON")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    scores = data.get("scores", {})
    overall = weighted_score(scores)
    evidence_count = int(data.get("evidence_count", 0))
    execution_count = int(data.get("real_world_execution_count", 0))
    delayed_days = int(data.get("delayed_review_days", 0))
    status, recommendation = classify(overall, execution_count, delayed_days)

    blockers: list[str] = []
    if evidence_count < 3:
        blockers.append("证据少于 3 条")
    if execution_count <= 0:
        blockers.append("缺少现实执行证据")
    if delayed_days < 7:
        blockers.append("缺少 7 天以上延迟保持验证")

    result = {
        "domain": data.get("domain", "unknown"),
        "internalization_score": overall,
        "dimension_scores": scores,
        "confidence": data.get("confidence", "low"),
        "status": status,
        "recommendation": recommendation,
        "evidence_count": evidence_count,
        "real_world_execution_count": execution_count,
        "delayed_review_days": delayed_days,
        "blockers": blockers,
        "handoff_to_persona_causal_evolver": status == "evolver_review_ready",
    }

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
