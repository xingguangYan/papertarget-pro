# ?? PaperTarget Pro V3 Ultimate

> **??????????? | Global Research Publishing Intelligence Agent**
> Version 3.0 Ultimate ? V4 Enhanced ? Multi-Platform Ready

[![GitHub Release](https://img.shields.io/github/v/release/xingguangYan/papertarget-pro)](https://github.com/xingguangYan/papertarget-pro/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-All%20AI%20Platforms-brightgreen)](#-multi-platform-deployment)

---

## ?? What Is PaperTarget Pro?

PaperTarget Pro V3 Ultimate is **not** a simple journal recommender. It is a **complete AI Research Publishing Intelligence Agent** ? a comprehensive system prompt + resource kit that transforms any LLM into a Senior Scientific Publishing Consultant.

It helps researchers **before submission** by performing:

- ? **Paper Quality Diagnosis** ? Automatic paper DNA construction, novelty assessment, value scoring
- ? **Intelligent Journal Matching** ? 10-layer matching algorithm (topic, method, citation, innovation, data scale, impact level, publication history, funding, country preference, editor preference)
- ? **Editorial Decision Simulation** ? Desk reject, major/minor revision, accept probability prediction
- ? **Reviewer Comment Prediction** ? Three simulated reviewers: methods expert, domain expert, statistics expert
- ? **Submission Success Rate Prediction** ? Acceptance rate, desk reject rate, revision likelihood
- ? **Cover Letter & Response Generation** ? SCI/SSCI/EI cover letters, transfer letters, appeal letters, bilingual response to reviewers
- ? **Rejection Rescue** ? Parse rejection letters, identify causes, recommend next journal
- ? **Academic Risk Control** ? Predatory journal detection, CAS warning, abnormal self-citation scoring
- ? **Career & Funding Matching** ? Graduation, promotion, talent plan, NSFC/NSF/NASA fund alignment
- ? **Full Journal Submission Intelligence Report** ? All analysis consolidated into one actionable report

**Final Goal: "Maximize acceptance probability + Maximize research impact"**

---

## ? Key Metrics

| Metric | Value |
|--------|-------|
| System Prompt Size | 1,791 words / ~13117 chars |
| Engine Modules | 20 integrated intelligence engines |
| Journal Matching Layers | 10-layer scoring system |
| Innovation Levels | 5 levels (L1: Follow-up ~ L5: Breakthrough) |
| Supported Input Modes | 10 (title, abstract, PDF, DOCX, LaTeX, rejection letter, etc.) |
| Simulated Reviewers | 3 (Methods, Domain, Statistics experts) |
| Publisher Simulations | 6 (Nature, Science, Cell, IEEE, Elsevier, Springer) |
| Knowledge Databases | 40+ international + 10+ Chinese databases |
| Evaluation Metrics | 20+ (JCR, CAS, IF, CiteScore, SJR, SNIP, CCF, FT50, etc.) |
| Supported Platforms | 7 (Cherry Studio, OpenWebUI, Dify, Coze, GPTs, Claude, Gemini) |

---

## ?? The 20 Core Engine Modules

| # | Module | Function |
|---|--------|----------|
| 1 | **Paper DNA Engine** | Automatically construct a Research DNA Tree with full discipline hierarchy |
| 2 | **Novelty Engine** | Diagnose innovation type (8 types) and level (L1-L5), output Innovation Index (0-100) |
| 3 | **Scientific Value Engine** | Assess academic, theoretical, engineering, industrial, policy, ecological, social value |
| 4 | **Publication Level Predictor** | Predict Q1-Q4, SCI/EI/SSCI, Chinese Core/CSCD fit with reasoning |
| 5 | **Journal Matching Engine** | 10-layer matching (Topic, Method, Citation, Innovation, Data, Impact, History, Funding, Country, Editor) |
| 6 | **Top Journal Recommender** | TOP 20 journals with 3-tier rating + 7 category-specific lists |
| 7 | **Editor Decision Simulator** | Simulate desk reject / accept / major revision / minor revision with probability |
| 8 | **Reviewer Brain Engine** | 3 simulated reviewers (Methods/Domain/Statistics expert) with full critique prediction |
| 9 | **Success Rate Engine** | Acceptance, rejection, major revision, minor revision, desk reject rates |
| 10 | **Time Prediction Engine** | Estimate initial review, external review, acceptance, online, print, total cycle |
| 11 | **Funding Match Engine** | NSFC, NSSFC, NSF, NASA, ESA, EU project alignment check |
| 12 | **Academic Career Engine** | Optimal submission pathway for graduation, PhD, promotion, talent plan |
| 13 | **Cover Letter Engine** | SCI/SSCI/EI/Chinese cover letters, transfer letters, appeal letters |
| 14 | **Response to Reviewers Engine** | Auto-generate bilingual point-by-point responses |
| 15 | **Rejection Rescue Engine** | Parse rejection, identify cause, recommend next journal, generate transfer |
| 16 | **Academic Risk Control** | CAS warning, predatory journal, self-citation, publisher risk scoring (0-100) |
| 17 | **Trend Forecast Engine** | 3/5/10 year hot topics, methods, data, models, funding analysis |
| 18 | **Competitor Analysis Engine** | Identify competing papers, teams, journals, authors + differentiation |
| 19 | **AI Review Score** | Nature/Science/Cell/IEEE/Elsevier editor simulation scoring |
| 20 | **Final Report** | Complete 15-section Journal Submission Intelligence Report |

---

## ?? V4 Enhancements

### ?? Real Journal Database (`references/journal_knowledge_base.md`)
- 60+ journals across 5 disciplines with IF, CAS quartile, APC costs ($500-$6,290)
- Typical review cycle reference (2-12 months) for each journal
- CAS Early Warning indicators and Publisher Risk Matrix
- Cross-reference to augment recommendation accuracy

### ?? Review Experience Mining (`scripts/search_review_data.py`)
- Generate targeted search queries for LetPub, Xiaomuchong, ResearchGate, SciRev
- Structured data collection template (review time, acceptance rate, editor profile)
- Subject-specific query generation (Remote Sensing, CS, Ecology, Medical)

### ?? Full-Text Paper Analysis (`scripts/analyze_paper.py`)
- Automatic text extraction from PDF, DOCX, LaTeX, TXT
- Section identification (Abstract, Introduction, Methods, Results, Discussion)
- Word count and structure analysis for quality diagnostics

### ?? Discipline-Specific Editions (`references/discipline_editions.md`)
- **Remote Sensing Edition**: Resolution, SAR/Optical, Foundation Models, Sentinel/Landsat data
- **Ecology Edition**: Experimental design, SEM, Species distribution, eDNA
- **Medical Edition**: Clinical trials, Ethics, Translational, Cohort validation
- **CS & AI Edition**: CCF tiers, Benchmarks, Ablation studies, Hot topics (LLM, Diffusion, AI4Science)

### ?? SCI Hit Rate Prediction Model
Built-in weighted scoring system using 6 dimensions:
- Innovation Score (20%) + Method Rigor (20%) + Data Quality (15%)
- Writing Quality (10%) + Topic Fit (15%) + Journal Match (20%)
- Output: Q1 Hit Rate, Top Journal Hit Rate, Desk Reject Risk, Revision Likelihood

---

## ?? Multi-Platform Deployment

PaperTarget Pro can be deployed to **all 7 major AI platforms**. Each platform folder contains ready-to-use files.

| Platform | Deployment File | Method | Effort |
|----------|----------------|--------|--------|
| ?? **Cherry Studio** | `deploy/cherry-studio/papertarget-pro.character.json` | Import JSON | ? 1-click |
| ?? **OpenWebUI** | `deploy/open-webui/function.py` + `manifest.json` | Admin > Functions > Import | ? 1-click |
| ?? **Dify** | `deploy/dify/agent-dsl.json` + `plugin.yaml` | Studio > Import DSL | ? 1-click |
| ?? **Coze** | `deploy/coze/bot-config.json` | Bot Studio > Copy config | ?? Manual (~5 min) |
| ?? **ChatGPT GPTs** | `deploy/chatgpt-gpts/gpts-manifest.json` | GPT Builder > Paste instructions | ?? Manual (~5 min) |
| ?? **Claude Projects** | `deploy/claude-projects/project-instructions.md` | New Project > Add instructions | ?? Manual (~3 min) |
| ?? **Gemini Gems** | `deploy/gemini-gems/gem-instructions.md` | Gems > Create > Paste | ?? Manual (~3 min) |

### Quick Deploy Commands

```bash
# Clone the repository
git clone https://github.com/xingguangYan/papertarget-pro.git
cd papertarget-pro

# Cherry Studio (auto-copy)
cp deploy/cherry-studio/papertarget-pro.character.json ~/.cherry-studio/characters/

# View all deployment files
ls deploy/*/
```

For **detailed step-by-step deployment instructions** (including screenshots and platform-specific settings), see the full [Deployment Guide](deploy/README.md).

---

## ?? Input Types

PaperTarget Pro supports 10 input modes ? just paste or upload what you have:

| # | Input Type | Best For |
|---|------------|----------|
| 1 | **Title only** | Quick journal direction check |
| 2 | **Title + Abstract** | Standard analysis (recommended minimum) |
| 3 | **Title + Abstract + Keywords** | More accurate matching |
| 4 | **Full-text PDF** | Comprehensive analysis (use `analyze_paper.py`) |
| 5 | **Full-text DOCX** | Comprehensive analysis (use `analyze_paper.py`) |
| 6 | **LaTeX source** | For TeX-native workflows |
| 7 | **Research direction** | When paper is not yet written |
| 8 | **Previously submitted journal** | For re-submission strategy |
| 9 | **Reviewer comments** | For response generation |
| 10 | **Rejection letter** | For rejection rescue analysis |

---

## ??? Usage Workflow

### Standard Workflow

```
User Input ? Paper DNA ? Novelty Engine ? Value Engine ? Level Predictor
    ? Journal Matching (10 layers) ? TOP 20 Recommender
    ? Editor Simulator ? Reviewer Brain ? Success Rate
    ? Risk Control ? Trend Forecast ? Funding & Career Match
    ? [Optional: Cover Letter / Response / Rejection Rescue]
    ? Final Journal Submission Intelligence Report
```

### Example Prompts

```text
"Here is my paper abstract: [paste abstract]. Please analyze it and recommend the best SCI journals for submission."

"My paper was rejected from Remote Sensing of Environment. Here is the rejection letter: [paste]. What should I do next?"

"Generate a Nature Communications cover letter for my paper titled: [title]."

"Simulate the three reviewers for my manuscript and predict what questions they will ask."

"I am a PhD student needing to graduate in 2 years. My research is on deep learning for land cover mapping. What is the optimal submission strategy?"
```

---

## ?? Repository Structure

```
papertarget-pro/
??? SKILL.md                          # Core system prompt (~14KB)
??? README.md                         # This file
??? LICENSE
??? agents/
?   ??? openai.yaml                   # Codex skill metadata
??? references/                       # Knowledge base (load for deeper analysis)
?   ??? journal_knowledge_base.md     # 60+ journals: IF, APC, review cycle, risk
?   ??? discipline_editions.md        # 4 discipline-specific evaluation models
??? scripts/                          # Utility scripts
?   ??? analyze_paper.py              # PDF/DOCX/LaTeX text extraction & analysis
?   ??? search_review_data.py         # Review experience mining query generator
??? deploy/                           # Multi-platform deployment artifacts
    ??? README.md                     # Step-by-step deployment guide
    ??? cherry-studio/                # ?? Import JSON
    ??? open-webui/                   # ?? Import Function
    ??? dify/                         # ?? Import DSL + Plugin
    ??? coze/                         # ?? Manual Bot setup
    ??? chatgpt-gpts/                 # ?? GPTs Builder config
    ??? claude-projects/              # ?? Project instructions
    ??? gemini-gems/                  # ?? Gem instructions
```

---

## ?? Knowledge Coverage

### International Databases (40+)
Web of Science Core Collection (SCIE, SSCI, AHCI, ESCI), Scopus, EI Compendex, PubMed, MEDLINE, Embase, IEEE Xplore, ACM DL, SpringerLink, ScienceDirect, Wiley Online Library, Nature Portfolio, Taylor & Francis, SAGE, MDPI, Frontiers, DOAJ, Google Scholar, Crossref, Dimensions, OpenAlex, Lens, ResearchGate, SciFinder, GeoRef, AGRIS, ADS, EconLit, INSPEC, JST, arXiv, SSRN, RePEc

### Chinese Databases (10+)
CNKI, CSCD, Peking University Core, Sci-Tech Core, Outstanding Journals, AMI, RCCSE, Wanfang, VIP, CSTPCD

### Evaluation Metrics (20+)
JCR, CAS (Chinese Academy of Sciences), Updated CAS, IF, 5-Year IF, Eigenfactor, Article Influence Score, CiteScore, SJR, SNIP, H-index, CCF, ABDC, ABS, FMS, FT50, UTD24, Google Scholar Metrics

---

## ?? Critical Rules

This skill follows 10 immutable rules for journal recommendation:

| # | Rule | Why It Matters |
|---|------|----------------|
| 1 | **Accuracy over Impact Factor** | IF is not the only quality metric |
| 2 | **Match quality over Journal Tier** | Best-fit journal > highest-ranked journal |
| 3 | **Acceptance probability over blind ambition** | Getting published > getting rejected |
| 4 | **Never sort by IF alone** | Multi-dimensional evaluation required |
| 5 | **Always explain recommendation rationale** | Transparent, actionable advice |
| 6 | **Always output risk analysis** | CAS warning, predatory risk, self-citation |
| 7 | **Always provide backup journals** | Plan B, C, D for every submission |
| 8 | **Distinguish: Reach vs Solid vs Safety** | Three-tier risk strategy |
| 9 | **Always evaluate OA cost, review cycle, acceptance rate, graduation/funding/career value** | Holistic evaluation |
| 10 | **Find "most worth submitting" journals, not "highest IF" journals** | The core philosophy |

---

## ?? Contributing

Contributions are welcome! Here are ways to help:

- **Add journals**: Submit PRs to `references/journal_knowledge_base.md` with verified data
- **New disciplines**: Add editions to `references/discipline_editions.md`
- **Scripts**: Improve `scripts/analyze_paper.py` or add new utilities
- **Translations**: Create translations of SKILL.md for other language communities
- **Bugs & Ideas**: Open [GitHub Issues](https://github.com/xingguangYan/papertarget-pro/issues)

---

## ?? Version History

| Version | Date | Highlights |
|---------|------|------------|
| v1.0 | 2024 | Original PaperTarget concept |
| v2.0 | 2024 Q3 | Expanded engine modules, multi-database integration |
| v3.0 | 2025 Q1 | 20 complete engine modules, full system prompt |
| v4.0 | 2025 Q2 | V4 Enhancements: Journal DB, Discipline Editions, Scripts, SCI Hit Rate |
| v4.0.1 | Current | Multi-platform deployment artifacts + GitHub Release |

---

## ?? Links

- **GitHub Repository**: [https://github.com/xingguangYan/papertarget-pro](https://github.com/xingguangYan/papertarget-pro)
- **GitHub Release**: [v4.0.0](https://github.com/xingguangYan/papertarget-pro/releases/tag/v4.0.0)
- **Deployment Guide**: [deploy/README.md](deploy/README.md)
- **Issues & Feedback**: [GitHub Issues](https://github.com/xingguangYan/papertarget-pro/issues)
- **Author**: [xingguangYan](https://github.com/xingguangYan)

---

## ?? License

MIT ? Free to use, modify, and distribute.

---

*Made with ?? for the global research community*