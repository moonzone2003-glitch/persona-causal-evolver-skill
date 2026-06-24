#!/usr/bin/env python3
"""Score a self-growth review from structured JSON input.

Input JSON schema:
{
  "domain": "investment",
  "scores": {"认知深度": 6, ...},
  "evidence_count": 5,
  "confidence": "medium",
  "notes": "optional"
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

DEFAULT_WEIGHTS = {
    "认知深度": 1.2,
    "信息质量": 1.0,
    "决策纪律": 1.2,
    "执行闭环": 1.1,
    "复盘能力": 1.0,
    "抗干扰能力": 0.9,
}

BANDS = [
    (3, "失控或未建立模型"),
    (5, "有意识但不稳定"),
    (7, "局部稳定，可形成方法"),
    (9, "稳定高手，可迁移复用"),
    (10, "专家级，可训练他人和系统化输出"),
]


def band(score: float) -> str:
    for upper, label in BANDS:
        if score <= upper:
            return label
    return BANDS[-1][1]


def weighted_score(scores: dict[str, float]) -> float:
    total_weight = 0.0
    weighted = 0.0
    for key, score in scores.items():
        weight = DEFAULT_WEIGHTS.get(key, 1.0)
        total_weight += weight
        weighted += max(0.0, min(10.0, float(score))) * weight
    if total_weight == 0:
        return 0.0
    return round(weighted / total_weight, 2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score self-growth review JSON")
    parser.add_argument("--input", required=True, help="Path to review JSON")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    scores = data.get("scores", {})
    overall = weighted_score(scores)
    evidence_count = int(data.get("evidence_count", 0))
    confidence = data.get("confidence", "low")
    evidence_penalty = "none"
    if evidence_count < 3 and confidence != "high":
        evidence_penalty = "low_evidence_mark_confidence_down"

    result = {
        "domain": data.get("domain", "unknown"),
        "overall_score": overall,
        "band": band(overall),
        "dimension_scores": scores,
        "confidence": confidence,
        "evidence_count": evidence_count,
        "evidence_penalty": evidence_penalty,
        "lowest_dimensions": sorted(scores.items(), key=lambda item: item[1])[:3],
    }

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
