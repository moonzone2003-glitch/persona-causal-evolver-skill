# 人格因果样本模板

```yaml
id: sample-001
date: YYYY-MM-DD
source:
  type: conversation | product | reflection | training-log | automation
  path_or_summary: ""
confidence: high | medium | low | noise
trigger: "发生了什么触发用户行动"
observed_behavior: "用户实际做了什么"
inferred_motive: "为什么这么做的假设"
personality_inference: "可能体现的稳定人格倾向"
desired_self: "想成为的样子或想避免的状态"
counter_evidence: "什么情况能推翻这个判断"
recommendation:
  action: write_to_persona | send_to_training | keep_as_observation | discard
  target: "目标 Skill 或训练领域"
```

## 最小 Markdown 输出

| 字段 | 内容 |
|---|---|
| 触发 |  |
| 行为 |  |
| 动机假设 |  |
| 人格推断 |  |
| 证据等级 |  |
| 反证条件 |  |
| 建议 |  |
