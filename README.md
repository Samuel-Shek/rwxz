# rwxz（人味写作）

Human-flavored writing skill for AI agents: create, rewrite, and polish copy that reads like a competent person wrote it.

## 它是什么

`rwxz`（别名 `renwei-xiezuo` / `renwei-writing`）是面向读者的文案 Skill：创作、改写、润色、去 AI 味、标题与大纲。默认在相关任务上自动启用，无需点名；用户明确说「不用 rwxz」才停用。

核心原则来自本仓库 `SKILL.md`：

- **信任先于刺激**：不编事实、不编故事，承认边界
- **先 brief 再动笔**：目的、读者、场景、文体、语气、篇幅、语言
- **按复杂度选流程**：轻量 / 标准 / 完整，短文案不强制调研
- **多语言**：按目标语言加载规则，不把中文习惯当成通用标准

当前版本见 `SKILL.md` 的 `metadata.version`（撰写本 README 时为 **3.3.1**）。

## 适用 / 不适用

**适用**：专业报告、微信公众号、邮件、社媒、产品文案、标题与大纲，以及「翻译后还要文案化」的改写。

**不适用（不强制触发）**：纯翻译、机械排版、代码、普通问答。用户要求逐字保真、仅排版、只审不改时，遵从用户约束。

本 Skill 只改写作方式，**不授予**发布、发送、账号操作或外发材料的权限。

## 安装与使用

把本仓库作为 Agent Skill 目录加载（不同宿主的目录名可能是 `skills/`、`.agents/skills/` 等）：

1. 克隆或复制本仓库到宿主可发现的 skills 路径，目录名建议为 `rwxz`
2. 确认根目录存在 `SKILL.md`
3. 在宿主中确认技能可被发现；需要时用别名 `/rwxz` 或 `/renwei-xiezuo` 显式调用

Codex / 兼容 OpenAI agents 元数据见 `agents/openai.yaml`（`allow_implicit_invocation: true`）。

## 目录结构

```
SKILL.md          # 主说明与行为规则
agents/           # 宿主元数据（如 openai.yaml）
locales/          # 语言包（zh-CN、en-US）
references/       # 渠道、语言与工具参考
  channels.md
  lang-zh.md
  lang-en.md
  lang-other.md
  research-prompts.md
  viral-toolkit.md
scripts/          # 辅助检查
  text_check.py   # 字数等检查
  zh_punct_fix.py
```

## 辅助脚本

```bash
python3 scripts/text_check.py count   # 按 SKILL 口径统计篇幅
```

具体子命令与参数以脚本 `--help` / 源码为准。

## License

本仓库根目录**未包含** LICENSE 文件；使用前请自行确认授权边界，或联系仓库所有者补充许可证。
