# Persona Causal Evolver Skill Pack

> 一套自我建模流水线：先用内置 `yourself-skill` 做初级人格蒸馏，再用 `persona-causal-evolver` 做高维因果进化，最后用 `self-growth-coach` 作为个人决策训练器，完成当前我、专家标杆、升维我、训练任务、内化评分和回灌裁决闭环。

## 包含什么

| 组件 | 是否内置 | 作用 |
|---|---|---|
| `yourself-skill` | 是，见 `skills/yourself-skill/` | 上游通用初级人格蒸馏 Skill，生成第一个“当前我” |
| `persona-causal-evolver` | 是，见 `skills/persona-causal-evolver/` | 从事件、文档、产物、checkpoint、训练记录中抽象人格因果 |
| `self-growth-coach` | 是，见 `skills/self-growth-coach/` | 个人决策训练器：把候选目标转成训练任务、评分、内化验证和复盘闭环 |

## 使用顺序

```text
复制/加载 skills/yourself-skill
→ 初级蒸馏当前我
→ 加载 skills/persona-causal-evolver
→ 从事件、产物、碰撞、Agent 文档中抽象候选人格规则
→ 加载 skills/self-growth-coach
→ 把未稳定目标转成训练任务
→ 训练结果再回到 persona-causal-evolver 复核
```

## 职责边界

| Skill | 适合独立使用的条件 | 不做什么 |
|---|---|---|
| `yourself-skill` | 首次建立自我模型 | 不负责长期因果进化 |
| `persona-causal-evolver` | 已有事件、文档、产物或初始自我 Skill 后 | 不做训练执行，不直接覆盖真实人格 |
| `self-growth-coach` | 已有训练目标或复盘场景后 | 不判断真实人格是否已经改变 |

> 注意：`persona-causal-evolver` 可以单独分析事件和产物，但首次人格蒸馏仍建议先用 `skills/yourself-skill`。如需跟随上游更新，也可以替换成本机已安装的新版 `yourself-skill`。

## 推荐仓库结构

```text
persona-causal-evolver-skill-pack/
  README.md
  .gitignore
  skills/
    yourself-skill/
      SKILL.md
      prompts/
      tools/
      selves/example_me/
    persona-causal-evolver/
      SKILL.md
      references/
      templates/
      examples/
      test-prompts.json
    self-growth-coach/
      SKILL.md
      config.json
      references/
      templates/
      scripts/
      data/
        sample-review.json
        sample-internalization.json
      test-prompts.json
```

## 不应上传的内容

- 个人真实人格 Skill，例如某个用户专属的自我模型。
- 私人记忆、聊天原文、交易/工作记录、checkpoint 原文、训练日志原文。
- 任何 `.env`、token、cookie、私有数据库。

## 数据边界

- 只保存摘要、证据指针、证据等级、反证条件和候选规则。
- 不保存、不回显原始敏感材料。
- 个人训练结果默认私有；公开仓库只放方法、模板和脱敏示例。

## 适合的输出

- 人格候选规则
- 证据等级判断
- 反证条件
- 回灌建议
- 训练任务和复盘模板

## 发布前检查

- `skills/persona-causal-evolver/examples/` 是否脱敏且不个人化。
- `skills/persona-causal-evolver/test-prompts.json` 是否覆盖负测。
- `skills/self-growth-coach/` 是否不包含私人训练日志。
- README 是否明确 `yourself-skill` 是外部前置依赖。
