# Paper2Slides (Academic Beamer Generator)

<div align="center">
  <a href="#english">English</a> | <a href="#简体中文">简体中文</a>
</div>

---

<h2 id="english">English</h2>

`paper2slides` is a specialized **AI Skill** designed for Claude Desktop or other LLM Agent systems. It automates the painful process of converting highly technical academic economics papers (working papers, PDFs, or LaTeX files) into clean, professional, and compilable LaTeX Beamer presentations within minutes.

### What is an AI Skill?
It is not a standalone executable software, but rather a structured bundle of **prompts, workflows, and templates**. By providing this folder as context to an advanced AI Agent, the AI gains the "expert capability" to distill papers into precise presentation slides, strictly adhering to predefined academic aesthetics and formula compression algorithms.

### Features
- **Intelligent Extraction:** Automatically identifies and extracts the core Motivation, Literature Review, Model Setup, Identification Strategy, and Main Results based on paper type (Theory, Empirical, or Structural).
- **Formula Compression:** Intelligently summarizes dense math blocks and proofs, keeping only the essential notation required for a presentation slide format.
- **Audience Calibration:** Automatically adjusts the density and slides count for Lightning Talks (5 mins), Conference Talks (15 mins), or full Seminars (60-90 mins).
- **Anti-Hallucination:** Built-in multi-round verification to ensure equations, citations, and empirical magnitudes reflect the actual source document.
- **Compilable Output:** Generates ready-to-use `.tex` source files (using the `metropolis` theme) or Markdown implementations for Marp/Reveal.js.

### Skill Structure
```text
paper2slides/
├── SKILL.md                                 # Main execution logic and trigger words
└── references/
    ├── extraction_protocol.md               # Rules for extracting content by paper type
    ├── slide_design_principles.md           # Academic presentation best practices 
    ├── compression_rules.md                 # Rules for reducing formula complexity
    └── beamer_templates.md                  # Baseline compilable LaTeX Beamer structures
```

### Installation / Integration

Since this is an AI Skill rather than a traditional Python/NPM package, "installation" means providing these files to your AI Agent's context window.

**For Claude Desktop / Claude Code:**
1. Clone this repository into a dedicated `skills` or `.claude/skills` directory in your workspace.
2. The AI will automatically read the `SKILL.md` when you mention the trigger words.

**For AntiGravity / Google Deepmind Agents:**
1. Clone the repository into your designated `workspace/skills` directory.
2. The agent's file-reading tools will automatically sweep this directory for tool augmentation.

**For Cursor / GitHub Copilot (Codex):**
1. Copy the `paper2slides` folder directly into your project's `.cursorrules` or `.github/prompts` references.
2. Ask the AI to "@paper2slides" to execute the instructions.

### How to Use
Once this skill directory is loaded into your Agent's context or Claude Desktop, trigger it simply by passing the path to an academic PDF or `.tex` file:

```bash
# Example user prompt:
paper2slides '/path/to/my_economics_working_paper.pdf'
```

You can customize the output via natural language:
> "Use `paper2slides` on this paper. Make it a 15-minute conference talk. Focus specifically on the robustness checks section and identification strategy."

### Output
The AI will generate a single, clean LaTeX code block that compiles directly into a PDF presentation:
- Uses the modern `metropolis` theme.
- Highlights key variables mathematically (e.g., `\alert{}`).
- Presenter notes are attached to each slide via `\note{}`.

---

<h2 id="简体中文">简体中文</h2>

`paper2slides` 是一个专门为 Claude Desktop 或其他大模型代理 (LLM Agent) 系统设计的 **AI Skill (人工智能技能包)**。它旨在自动化一个极其耗时的过程：将高度专业化的学术论文（包含公式密集的 Working Papers、PDF 或 LaTeX 源码）在几分钟内转化为干净、专业、可直接编译的 LaTeX Beamer 学术演示幻灯片。

### 什么是 AI Skill (技能)?
它不是一个传统的独立可执行软件，而是一个结构化的**提示词、工作流与模板的集合**。在您的本地 Claude 桌面端或 AI Agent 工作区中，只需将此文件夹作为上下文提供给 AI，AI 即可获得“将论文降维成精准 Slides”的专家级能力，严格遵循预设的学术审美和公式压缩算法。

### 核心功能
- **智能提取:** 根据论文类型（理论、实证或结构模型），自动识别并提取核心的 Motivation、文献定位、模型设定、识别策略 (Identification Strategy) 和主要结果。
- **公式压缩:** 智能摘要密集的数学推导和证明，仅保留在有限幻灯片演示中必不可少的核心符号与直觉。
- **受众与时长校准:** 针对闪电演讲 (Lightning Talk, 5分钟)、学术会议 (Conference Talk, 15分钟) 或完整研讨会 (Seminar, 60-90分钟) 自动调整内容密度。
- **反幻觉自我核查 (Anti-Hallucination):** 内置多轮自我验证工作流，确保生成的方程式、引用和实证估计数值与原始文档绝对一致。
- **可编译输出:** 生成即插即用、结构完美的 `.tex` 源码（采用现代学术界标配的 `metropolis` 主题），或支持 Marp/Reveal.js 渲染的 Markdown。

### 技能包目录结构
```text
paper2slides/
├── SKILL.md                                 # 核心大模型执行逻辑、系统提示词与触发词
└── references/
    ├── extraction_protocol.md               # 针对不同论文大类的内容提取硬性规则
    ├── slide_design_principles.md           # 学术 Slide 排版最佳实践 (一页一重点等)
    ├── compression_rules.md                 # 减少数学公式复杂度的降维原则
    └── beamer_templates.md                  # 基础可编译的 LaTeX Beamer 骨架模板
```

### 安装与集成 (Installation)

由于这是一个 AI Skill 而非传统的 Python/NPM 软件包，“安装”本质上是将这些文件放入您的 AI 代理 (Agent) 能够读取的上下文目录中。

**适用于 Claude Desktop / Claude Code:**
1. 将此仓库克隆到您工作区专门的 `skills` 或 `.claude/skills` 文件夹中。
2. 当您在对话中提到触发词时，Claude 会自动读取 `SKILL.md`。

**适用于 AntiGravity / Google Agents:**
1. 将此仓库克隆到您的工作区 `workspace/skills` 目录下。
2. Agent 会通过其内部的工具链自动扫描并挂载此项技能。

**适用于 Cursor / GitHub Copilot (Codex):**
1. 将 `paper2slides` 文件夹直接放入项目根目录，并在您的 `.cursorrules` 中引用。
2. 在对话框中输入 `@paper2slides` 即可唤醒并执行相关指令。

### 如何使用
如果您的 AI (比如我们配置的 Agent 环境) 已经接入了此技能目录，您只需在对话框中传入论文路径或文档即可触发：

```bash
# 用户 Prompt 示例:
paper2slides '/path/to/my_economics_working_paper.pdf'
```

您可以通过自然语言指定各种定制参数：
> "请调用 `paper2slides` 处理这篇论文。帮我生成一个 15 分钟的 Conference Talk 幻灯片。对方是审稿人，请特别侧重展示 Robustness Checks 和识别策略的部分。"

### 输出结果
大模型最终将输出一个单一的、干净的 LaTeX 代码块。您只需复制或另存为 `.tex` 编译即可：
- 使用现代的扁平化极简主题 `metropolis`。
- 实证方程中的核心变量自动使用醒目颜色高亮（如红色 `\alert{}`）。
- 每张幻灯片底部自动生成对应的口语化演讲草稿 (`\note{}`).

---
*Built with the Grant Copilot mindset — Designed by economists, for economists.*
