#!/usr/bin/env python3
"""Generate 5/8/10 future-self contrast prompts for a scenario."""
from __future__ import annotations

import argparse
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build future-self contrast scaffold")
    parser.add_argument("--domain", required=True)
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()

    scaffold = {
        "domain": args.domain,
        "scenario": args.scenario,
        "contrast": {
            "5分的我": {
                "focus": "直觉、兴奋点、局部信息、短期反馈",
                "risk": "证据不足时提前行动，复盘时偏结果归因",
                "question": "我现在最可能忽略的反证是什么？",
            },
            "8分的我": {
                "focus": "证据链、触发条件、纪律、最小试错",
                "risk": "可能仍依赖人工提醒才能完全闭环",
                "question": "满足哪些条件才允许行动？",
            },
            "10分的我": {
                "focus": "系统化规则、预案、反证、复用沉淀",
                "risk": "避免过度系统化导致行动迟缓",
                "question": "这次判断能沉淀成什么可复用规则？",
            },
        },
        "next_step": "先补证据，再定条件，最后只执行一个最小动作。",
    }
    print(json.dumps(scaffold, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
