# 安装说明

## 1. 复制本仓库内置 Skill

将以下三个目录复制到你的 Agent Skill 目录：

```text
skills/yourself-skill/
skills/persona-causal-evolver/
skills/self-growth-coach/
```

示例目标结构：

```text
~/.workbuddy/skills/
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
  self-growth-coach/
    SKILL.md
    config.json
    references/
    templates/
    scripts/
```

说明：`skills/yourself-skill/selves/example_me/` 是上游通用示例，不是真人用户数据。你可以保留它作为格式参考，也可以安装时删除。

## 2. 使用顺序

```text
yourself-skill
→ 生成初始自我 Skill
→ persona-causal-evolver
→ self-growth-coach
→ persona-causal-evolver 复核训练结果
```

## 3. 可选：替换上游新版 yourself-skill

本仓库内置的是通用 `yourself-skill` 副本。若你已经从上游安装了更新版本，可以用新版替换：

```text
skills/yourself-skill/
```

替换前请确认：

- 不包含真实个人 self/persona 产物。
- 不包含聊天原文、照片原图、日志原文。
- 不包含 token、cookie、私有路径或平台账号信息。

## 4. 隐私边界

不要把个人真实人格 Skill、聊天原文、checkpoint 原文、训练日志原文提交到公开仓库。

公开仓库只应包含：

- 方法说明
- 通用 Skill 代码
- 脱敏模板
- 示例样本
- 测试 prompts
- 不含个人数据的脚本
