# PaperTarget Pro V3 Ultimate

> **Global Research Publishing Intelligence Agent**  
> Version 3.0 Ultimate | V4 Enhanced | Multi-Platform Ready

[![Release](https://img.shields.io/github/v/release/xingguangYan/papertarget-pro)](https://github.com/xingguangYan/papertarget-pro/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

## Table of Contents

1. [What Is PaperTarget Pro?](#what-is-papertarget-pro)
2. [Key Metrics](#key-metrics)
3. [The 20 Core Engine Modules](#the-20-core-engine-modules)
4. [V4 Enhancements](#v4-enhancements)
5. [Multi-Platform Deployment](#multi-platform-deployment)
6. [Input Types](#input-types)
7. [Usage Guide](#usage-guide)
8. [Knowledge Coverage](#knowledge-coverage)
9. [Critical Rules](#critical-rules)
10. [Repository Structure](#repository-structure)
11. [Contributing](#contributing)
12. [License](#license)

---

## What Is PaperTarget Pro?

PaperTarget Pro V3 Ultimate is **not** a simple journal recommender. It is a **complete AI Research Publishing Intelligence Agent** - a comprehensive system prompt plus resource kit that transforms any AI assistant into a Senior Scientific Publishing Consultant.

It helps researchers **before submission** by performing:

| Capability | Description |
|------------|-------------|
| Paper Quality Diagnosis | Automatic paper DNA construction, novelty assessment, value scoring |
| Intelligent Journal Matching | 10-layer matching algorithm (topic, method, citation, innovation, data, impact, history, funding, country, editor) |
| Editorial Decision Simulation | Desk reject, major/minor revision, accept probability prediction |
| Reviewer Comment Prediction | 3 simulated reviewers: methods expert, domain expert, statistics expert |
| Success Rate & Time Prediction | Acceptance rate, review timeline, publication cycle estimation |
| Cover Letter & Response Generation | SCI/SSCI/EI cover letters, transfer letters, appeal letters, bilingual reviewer responses |
| Rejection Rescue | Parse rejection letters, identify causes, recommend next journal |
| Academic Risk Control | Predatory journal detection, CAS warning, abnormal self-citation scoring |
| Career & Funding Matching | Graduation, promotion, talent plan, NSFC/NSF/NASA fund alignment |
| Final Intelligence Report | Complete 15-section Journal Submission Intelligence Report |

**Final Goal: "Maximize acceptance probability + Maximize research impact"**

---

## Key Metrics

| Metric | Value |
|--------|-------|
| System Prompt Size | 1,791 words / ~13KB |
| Engine Modules | 20 integrated intelligence engines |
| Journal Matching Layers | 10-layer scoring system |
| Innovation Levels | L1 (Follow-up) through L5 (Original Breakthrough) |
| Input Modes | 10 (title, abstract, PDF, DOCX, LaTeX, rejection letter, etc.) |
| Simulated Reviewers | 3 (Methods, Domain, Statistics) |
| Publisher Simulations | 6 (Nature, Science, Cell, IEEE, Elsevier, Springer) |
| Knowledge Databases | 40+ international + 10+ Chinese |
| Evaluation Metrics | 20+ (JCR, CAS, IF, CiteScore, SJR, SNIP, CCF, FT50, etc.) |
| Supported Platforms | 7 platforms |

---

## The 20 Core Engine Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | **Paper DNA Engine** | Build Research DNA Tree with full discipline hierarchy, methodology, data sources, and innovation points |
| 2 | **Novelty Engine** | Classify innovation into 8 types (Incremental through Paradigm) and 5 levels (L1-L5), output Innovation Index 0-100 |
| 3 | **Scientific Value Engine** | Assess value across 7 dimensions: academic, theoretical, engineering, industrial, policy, ecological, social |
| 4 | **Publication Level Predictor** | Predict Q1-Q4 tier, SCI/EI/SSCI classification, Chinese Core/CSCD fit with full reasoning |
| 5 | **Journal Matching Engine** | 10-layer scoring: Topic, Method, Citation, Innovation, Data Scale, Impact Level, Publication History, Funding, Country, Editor Preference |
| 6 | **Top Journal Recommender** | TOP 20 with three-tier rating + 7 category-specific lists (Chinese, SCI, EI, OA, Non-OA, Graduation, Fast-Track) |
| 7 | **Editor Decision Simulator** | Probability-weighted simulation of Desk Reject, Accept, Major/Minor Revision with rationale and risk points |
| 8 | **Reviewer Brain Engine** | 3 simulated reviewers (Methods Expert, Domain Expert, Statistics Expert) with full critique prediction |
| 9 | **Success Rate Engine** | Percentages for acceptance, rejection, major revision, minor revision, desk reject |
| 10 | **Time Prediction Engine** | Timeline estimates for initial review, external review, major revision, acceptance, online, print, total cycle |
| 11 | **Funding Match Engine** | Check alignment with NSFC, NSSFC, MOE, NSF, NASA, ESA, EU project requirements |
| 12 | **Academic Career Engine** | Generate optimal submission pathway for graduation, PhD application, promotion, talent plan, overseas applications |
| 13 | **Cover Letter Engine** | Generate SCI/SSCI/EI/Chinese cover letters, transfer letters, and appeal letters |
| 14 | **Response to Reviewers Engine** | Auto-generate bilingual (Chinese + English) point-by-point responses to reviewer comments |
| 15 | **Rejection Rescue Engine** | Parse rejection letters, identify root causes, recommend next journal, recalculate success rates, generate transfer materials |
| 16 | **Academic Risk Control** | Score (0-100) for CAS warning, predatory journals, abnormal self-citation, publication volume, discontinuation risk, publisher risk |
| 17 | **Trend Forecast Engine** | Analyze 3/5/10 year hot topics, methods, data, models, and funding directions; predict future trends |
| 18 | **Competitor Analysis Engine** | Identify competing papers, teams, journals, and authors; provide differentiation recommendations |
| 19 | **AI Review Score** | Simulate Nature/Science/Cell/IEEE/Elsevier/Springer editor scoring across originality, rigor, impact, publishability |
| 20 | **Final Report** | Compile comprehensive 15-section Journal Submission Intelligence Report |

---

## V4 Enhancements

### Journal Database (references/journal_knowledge_base.md)
- 60+ journals across 5 disciplines with IF, CAS quartile, and APC costs (-,290)
- Typical review cycle reference (2-12 months) per journal
- CAS Early Warning indicators and Publisher Risk Matrix

### Review Experience Mining (scripts/search_review_data.py)
- Generate targeted queries for LetPub, Xiaomuchong, ResearchGate, SciRev
- Structured data collection template (review time, acceptance rate, editor profile)
- Discipline-specific query generation

### Full-Text Paper Analysis (scripts/analyze_paper.py)
- Extract text from PDF, DOCX, LaTeX, TXT automatically
- Identify paper sections (Abstract, Introduction, Methods, Results, Discussion)
- Word count and structure analysis for quality diagnostics

### Discipline-Specific Editions (references/discipline_editions.md)
- **Remote Sensing**: Resolution, SAR/Optical, Foundation Models, Sentinel/Landsat
- **Ecology**: Experimental design, SEM, Species distribution, eDNA
- **Medical**: Clinical trials, Ethics, Translational, Cohort validation
- **CS & AI**: CCF tiers, Benchmarks, Ablation studies, LLM/Diffusion/AI4Science

### SCI Hit Rate Prediction Model
Weighted 6-dimension scoring:
- Innovation (20%) + Method Rigor (20%) + Data Quality (15%)
- Writing Quality (10%) + Topic Fit (15%) + Journal Match (20%)
- Output: Q1 rate, Top Journal rate, Desk Reject risk, Revision likelihood

---

## Multi-Platform Deployment

PaperTarget Pro can be deployed to **7 major AI platforms**. Each has ready-to-use files in deploy/.

| Platform | File | Method | Time |
|----------|------|--------|------|
| Cherry Studio | deploy/cherry-studio/papertarget-pro.character.json | Import JSON | 1-click |
| OpenWebUI | deploy/open-webui/function.py + manifest.json | Admin Panel > Functions > Import | 1-click |
| Dify | deploy/dify/agent-dsl.json + plugin.yaml | Studio > Import DSL | 1-click |
| Coze | deploy/coze/bot-config.json | Bot Studio > manual config | ~5 min |
| ChatGPT GPTs | deploy/chatgpt-gpts/gpts-manifest.json | GPT Builder > paste instructions | ~5 min |
| Claude Projects | deploy/claude-projects/project-instructions.md | New Project > add instructions | ~3 min |
| Gemini Gems | deploy/gemini-gems/gem-instructions.md | Gems > Create > paste | ~3 min |

`
# Quick clone
git clone https://github.com/xingguangYan/papertarget-pro.git
cd papertarget-pro
# Full deployment guide: deploy/README.md
`

---

## Input Types

| # | Input | Best For |
|---|-------|----------|
| 1 | Title only | Quick journal direction check |
| 2 | Title + Abstract | Standard analysis (recommended minimum) |
| 3 | Title + Abstract + Keywords | More accurate matching |
| 4 | Full-text PDF | Comprehensive analysis |
| 5 | Full-text DOCX | Comprehensive analysis |
| 6 | LaTeX source | TeX-native workflows |
| 7 | Research direction | Before paper is written |
| 8 | Previously submitted journal | Re-submission strategy |
| 9 | Reviewer comments | Response generation |
| 10 | Rejection letter | Rescue analysis |

---

## Usage Guide

### Standard Workflow

User Input > Paper DNA > Novelty Engine > Value Engine > Level Predictor > Journal Matching (10 layers) > TOP 20 Recommender > Editor Simulator > Reviewer Brain > Success Rate > Risk Control > Trend Forecast > Funding & Career Match > [Optional: Cover Letter / Response / Rejection Rescue] > Final Report

### Example Prompts

`
"Here is my paper abstract: [paste]. Please analyze it and recommend the best SCI journals."

"My paper was rejected from Remote Sensing of Environment. Here is the rejection letter: [paste]. What should I do next?"

"Generate a Nature Communications cover letter for my paper titled: [title]."

"Simulate three reviewers for my manuscript and predict what questions they will ask."

"I am a PhD student needing to graduate in 2 years. My research is on deep learning for land cover mapping. What is the optimal submission strategy?"
`

---

## Knowledge Coverage

### International Databases (40+)
Web of Science Core Collection (SCIE, SSCI, AHCI, ESCI), Scopus, EI Compendex, PubMed, MEDLINE, Embase, IEEE Xplore, ACM DL, SpringerLink, ScienceDirect, Wiley Online Library, Nature Portfolio, Taylor & Francis, SAGE, MDPI, Frontiers, DOAJ, Google Scholar, Crossref, Dimensions, OpenAlex, Lens, ResearchGate, SciFinder, GeoRef, AGRIS, ADS, EconLit, INSPEC, JST, arXiv, SSRN, RePEc

### Chinese Databases (10+)
CNKI, CSCD, Peking University Core, Sci-Tech Core, Outstanding Journals, AMI, RCCSE, Wanfang, VIP, CSTPCD

### Evaluation Metrics (20+)
JCR, CAS, Updated CAS, IF, 5-Year IF, Eigenfactor, Article Influence Score, CiteScore, SJR, SNIP, H-index, CCF, ABDC, ABS, FMS, FT50, UTD24, Google Scholar Metrics

---

## Critical Rules

| # | Rule | Why |
|---|------|-----|
| 1 | Accuracy over Impact Factor | IF is not the only quality metric |
| 2 | Match quality over Journal Tier | Best-fit > highest-ranked |
| 3 | Acceptance probability over blind ambition | Published > rejected |
| 4 | Never sort by IF alone | Multi-dimensional evaluation required |
| 5 | Always explain recommendation rationale | Transparent, actionable advice |
| 6 | Always output risk analysis | CAS warning, predatory risk, self-citation |
| 7 | Always provide backup journals | Plan B, C, D for every submission |
| 8 | Distinguish: Reach vs Solid vs Safety | Three-tier risk strategy |
| 9 | Evaluate OA cost, review cycle, acceptance rate, graduation/funding/career value | Holistic evaluation |
| 10 | Find most worth submitting journals, not highest IF journals | Core philosophy |

---

## Repository Structure

`
papertarget-pro/
|-- SKILL.md                          # Core system prompt (~14KB)
|-- README.md                         # This file
|-- agents/
|   +-- openai.yaml                   # Codex skill metadata
|-- references/                       # Knowledge base
|   |-- journal_knowledge_base.md     # 60+ journals: IF, APC, review cycle, risk
|   +-- discipline_editions.md        # 4 discipline-specific evaluation models
|-- scripts/                          # Utility scripts
|   |-- analyze_paper.py              # PDF/DOCX/LaTeX text extraction
|   +-- search_review_data.py         # Review experience mining
+-- deploy/                           # Platform deployment artifacts
    |-- README.md                     # Deployment guide
    |-- cherry-studio/                # Import JSON
    |-- open-webui/                   # Import Function
    |-- dify/                         # Import DSL + Plugin
    |-- coze/                         # Manual Bot setup
    |-- chatgpt-gpts/                 # GPTs Builder config
    |-- claude-projects/              # Project instructions
    +-- gemini-gems/                  # Gem instructions
`

---

## Version History

| Version | Highlights |
|---------|------------|
| v1.0 | Original PaperTarget concept |
| v2.0 | Expanded engine modules, multi-database integration |
| v3.0 | 20 complete engine modules, full system prompt |
| v4.0 | V4 Enhancements: Journal DB, Discipline Editions, Scripts, SCI Hit Rate |
| v4.0.1 | Multi-platform deployment artifacts + GitHub Release |

---

## Contributing

Contributions welcome!
- Add journals: Submit PRs to references/journal_knowledge_base.md
- New disciplines: Add editions to references/discipline_editions.md
- Improve scripts: Enhance analyze_paper.py or add new utilities
- Report issues: Open GitHub Issues

---

## Links

- **Repository**: [github.com/xingguangYan/papertarget-pro](https://github.com/xingguangYan/papertarget-pro)
- **Release**: [v4.0.0](https://github.com/xingguangYan/papertarget-pro/releases/tag/v4.0.0)
- **Deployment Guide**: [deploy/README.md](deploy/README.md)
- **Author**: [xingguangYan](https://github.com/xingguangYan)

---

## License

MIT - Free to use, modify, and distribute.

---

Made with love for the global research community.