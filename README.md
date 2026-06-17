# PaperTarget Pro V3 Ultimate

> **Global Research Publishing Intelligence Agent** | Version: 3.0 Ultimate [V4 Enhanced]

PaperTarget Pro V3 Ultimate is a Codex Skill ? an AI Research Publishing Intelligence Agent that helps researchers maximize both acceptance probability and scientific impact through 20 integrated engine modules plus V4 enhancements.

## Features

- **20 Core Engine Modules**: Paper DNA, Novelty, Scientific Value, Journal Matching (10-layer), Editor Simulation, Reviewer Brain, Success Prediction, and more
- **V4 Enhancements**: Journal database, review experience mining, full-text analysis, discipline editions, SCI hit rate prediction
- **Multi-Platform Support**: Deployable to Cherry Studio, OpenWebUI, Dify, Coze, ChatGPT GPTs, Claude Projects, Gemini Gems

## Multi-Platform Deployment

This skill can be deployed to ALL major AI platforms:

| Platform | File | Status |
|----------|------|--------|
| Cherry Studio | `deploy/cherry-studio/papertarget-pro.character.json` | Import JSON |
| OpenWebUI | `deploy/open-webui/function.py` + `manifest.json` | Import Function |
| Dify | `deploy/dify/agent-dsl.json` + `plugin.yaml` | Import DSL/Plugin |
| Coze | `deploy/coze/bot-config.json` | Manual bot setup |
| ChatGPT GPTs | `deploy/chatgpt-gpts/gpts-manifest.json` | GPT Builder manual |
| Claude Projects | `deploy/claude-projects/project-instructions.md` | Manual setup |
| Gemini Gems | `deploy/gemini-gems/gem-instructions.md` | Manual setup |

**Full instructions:** See [Deployment Guide](deploy/README.md)

## Quick Start

```bash
# Clone the repo
git clone https://github.com/xingguangYan/papertarget-pro.git

# Analyze a paper
python scripts/analyze_paper.py paper.pdf

# Search review experience
python scripts/search_review_data.py --journal "Nature Communications"

# Then use the skill on any platform
```

## Repository Structure

```
papertarget-pro/
??? SKILL.md                    # Full system prompt (use anywhere)
??? README.md
??? agents/
?   ??? openai.yaml
??? references/
?   ??? journal_knowledge_base.md   # 4.9KB journal DB
?   ??? discipline_editions.md       # 5.4KB domain-specific models
??? scripts/
?   ??? analyze_paper.py             # PDF/DOCX/LaTeX extractor
?   ??? search_review_data.py        # Review experience miner
??? deploy/                          # Multi-platform deployment artifacts
    ??? README.md                    # Deployment guide
    ??? cherry-studio/
    ??? open-webui/
    ??? dify/
    ??? coze/
    ??? chatgpt-gpts/
    ??? claude-projects/
    ??? gemini-gems/
```

## License

MIT