# 决策训练输出模板

结论：本轮训练的核心差距是 `{core_gap}`，本轮只训练 `{training_focus}`。

## 1. 证据范围

| 项 | 内容 |
|---|---|
| 领域 | {domain} |
| 场景 | {scenario} |
| 证据来源 | {evidence_sources} |
| 可信度 | {confidence} |
| 数据缺口 | {missing_evidence} |

## 2. 三方对照

| 角色 | 判断 | 理由 | 风险控制 | 下一步动作 |
|---|---|---|---|---|
| 当前我 | {current_self_decision} | {current_self_reasoning} | {current_self_risk_control} | {current_self_action} |
| 专家标杆 | {expert_decision} | {expert_reasoning} | {expert_risk_control} | {expert_action} |
| 升维我 | {upgraded_self_decision} | {upgraded_self_reasoning} | {upgraded_self_risk_control} | {upgraded_self_action} |

## 3. 差距归因

| 差距 | 属于哪类能力 | 证据 | 反证条件 |
|---|---|---|---|
| {gap} | {capability} | {evidence} | {counter_evidence} |

## 4. 本轮训练

| 训练动作 | 做法 | 通过标准 | 复盘问题 |
|---|---|---|---|
| {task} | {method} | {pass_criteria} | {review_question} |

## 5. 内化验证

| 维度 | 评分 | 证据 |
|---|---:|---|
| 理解 | {understanding_score} | {understanding_evidence} |
| 迁移 | {transfer_score} | {transfer_evidence} |
| 决策改善 | {decision_score} | {decision_evidence} |
| 执行 | {execution_score} | {execution_evidence} |
| 保持 | {retention_score} | {retention_evidence} |

## 6. 回流建议

- 写入 `profiles/`：{profile_candidate}
- 写入训练日志：{training_log_summary}
- 交给 `persona-causal-evolver`：{evolver_handoff}
- 不得回灌真实人格的原因：{no_direct_persona_write_reason}
