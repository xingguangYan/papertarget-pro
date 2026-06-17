# PaperTarget Pro V3 Ultimate ? Multi-Platform Deployment Guide

> Deploy the AI Research Publishing Intelligence Agent to ALL major AI platforms.

## Platform Summary

| Platform | File | Deployment Method | Store Available? |
|----------|------|-------------------|------------------|
| **Cherry Studio** | `deploy/cherry-studio/papertarget-pro.character.json` | Import JSON file | Yes (local) |
| **OpenWebUI** | `deploy/open-webui/manifest.json` + `function.py` | Admin panel import | Yes (community) |
| **Dify** | `deploy/dify/plugin.yaml` + `agent-dsl.json` | Plugin/Agent import | Yes (marketplace) |
| **Coze** | `deploy/coze/bot-config.json` | Create bot + manual config | Yes (bot store) |
| **ChatGPT (GPTs)** | `deploy/chatgpt-gpts/gpts-manifest.json` | GPT Builder (manual) | Yes (GPT Store) |
| **Claude Projects** | `deploy/claude-projects/project-instructions.md` | Project settings | No |
| **Gemini Gems** | `deploy/gemini-gems/gem-instructions.md` | Gem settings | No |

---

## 1. Cherry Studio (????)

Cherry Studio is a desktop AI client that supports local character import.

### Steps:
1. Open Cherry Studio
2. Go to **Settings ? Character Management ? Import**
3. Select `deploy/cherry-studio/papertarget-pro.character.json`
4. The character will appear in your character list
5. Click to start a conversation with PaperTarget Pro

### Auto-deploy command (if Cherry Studio CLI available):
```bash
# Copy to Cherry Studio character directory
cp deploy/cherry-studio/papertarget-pro.character.json ~/.cherry-studio/characters/
```

---

## 2. OpenWebUI (Function Import)

OpenWebUI supports custom functions that inject system prompts.

### Steps:
1. Open your OpenWebUI instance
2. Go to **Admin Panel ? Functions**
3. Click **+ Import Function**
4. Upload `deploy/open-webui/function.py`
5. The manifest.json will be auto-detected from the function metadata
6. Enable the function and select it in your chat session

### Manual Setup (alternative):
1. Create a new model in OpenWebUI
2. Paste the contents of `deploy/open-webui/manifest.json` as instructions
3. Add the references as Knowledge files

---

## 3. Dify (Plugin/Agent Import)

Dify supports custom plugins and agent DSL imports.

### Method A: Agent DSL Import (Recommended)
1. Open your Dify workspace
2. Go to **Studio ? Create Agent ? Import DSL**
3. Select `deploy/dify/agent-dsl.json`
4. The agent will be created with the complete system prompt
5. Add knowledge documents: upload `references/journal_knowledge_base.md` and `references/discipline_editions.md`

### Method B: Plugin Import
1. Go to **Plugin Marketplace ? Install from Local File**
2. Select `deploy/dify/plugin.yaml`
3. Enable the plugin in your workspace

---

## 4. Coze Bot (Bot Creation)

Coze requires manual bot creation via the web interface, but the config file provides all settings.

### Steps:
1. Go to [Coze Bot Studio](https://www.coze.com) (or [coze.cn](https://www.coze.cn) for China)
2. Click **Create Bot**
3. Bot Name: `PaperTarget Pro V3 Ultimate`
4. Icon: ??
5. **Persona & Response**: Open `deploy/coze/bot-config.json` and copy the `prompt` field
6. Set Opening Dialog from config's `opening_dialog` field
7. Add Suggested Questions from config's `suggested_questions` field
8. **Knowledge**: Upload `references/journal_knowledge_base.md` and `references/discipline_editions.md`
9. **Model**: Select GPT-4o or Claude 3.5 Sonnet, temperature 0.7
10. Click **Publish** to submit to Coze Bot Store

---

## 5. ChatGPT GPTs (GPT Store)

GPTs require a ChatGPT Plus/Pro account and manual setup via the GPT Builder.

### Steps:
1. Go to [ChatGPT GPT Builder](https://chatgpt.com/gpts/editor)
2. Configure the GPT:
   - **Name**: PaperTarget Pro V3 Ultimate
   - **Description**: AI Research Publishing Intelligence Agent
   - **Instructions**: Open `deploy/chatgpt-gpts/gpts-manifest.json` and copy the `instructions` field
   - **Conversation starters**: Use the `conversation_starters` from the manifest
3. Enable capabilities: **Web Browsing** (for journal data lookup)
4. **Knowledge**: Upload `references/journal_knowledge_base.md`
5. Click **Save** and optionally **Publish to GPT Store**

---

## 6. Claude Projects

Claude Projects support custom instructions and knowledge files.

### Steps:
1. Open [Claude](https://claude.ai)
2. Go to **Projects ? Create Project**
3. Project Name: `PaperTarget Pro V3 Ultimate`
4. **Project Instructions**: Copy contents of `deploy/claude-projects/project-instructions.md`
5. **Knowledge**: Upload:
   - `SKILL.md` (full system prompt)
   - `references/journal_knowledge_base.md`
   - `references/discipline_editions.md`
6. Click **Create Project**
7. Start a conversation: Type or paste your paper details

---

## 7. Gemini Gems

Gemini Gems is Googles custom AI assistant feature.

### Steps:
1. Open [Gemini](https://gemini.google.com)
2. Go to **Settings ? Gems ? Create Gem**
3. **Gem Name**: PaperTarget Pro V3 Ultimate
4. **Instructions**: Copy contents of `deploy/gemini-gems/gem-instructions.md`
5. Click **Save**
6. Select the Gem from the dropdown and start your session

---

## One-Click Quick Deploy (Local)

If you use Cherry Studio or have CLI access to any platform:

```bash
# Cherry Studio
cp deploy/cherry-studio/papertarget-pro.character.json ~/.cherry-studio/characters/

# Clone the repo for all files
git clone https://github.com/xingguangYan/papertarget-pro.git
cd papertarget-pro

# View all deployable artifacts
ls deploy/*/
```

---

## Release Notes

| Version | Date | Changes |
|---------|------|---------|
| v3.0.0 | 2025 Q1 | Initial release - 20 core engine modules |
| v4.0.0 | 2025 Q2 | Journal DB, Review Mining, Discipline Editions, SCI Hit Rate |
| v4.0.1 | Current | Multi-platform deployment artifacts |

---

## Links

- GitHub: [https://github.com/xingguangYan/papertarget-pro](https://github.com/xingguangYan/papertarget-pro)
- Issues/Feedback: [GitHub Issues](https://github.com/xingguangYan/papertarget-pro/issues)
- Author: [xingguangYan](https://github.com/xingguangYan)