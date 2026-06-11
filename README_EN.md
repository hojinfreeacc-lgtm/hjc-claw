# 🦅 HJC CLAW (v1.2.0)

**HJC CLAW** is a **Hybrid AI Automation Agent** that combines local OS control, system automation, and powerful AI reasoning. It integrates the execution power of Open Interpreter with a local-first, security-centric design to intelligently manage your PC.

---

## ✨ Key Features

- **🧠 Multi-AI Brain:** Supports Google Gemini, OpenAI, and local Gemma (via Ollama), allowing you to choose the best AI for your needs.
- **💻 Dynamic Interpreter:** For complex commands beyond predefined rules, the AI generates Python code on-the-fly and executes it safely.
- **🛡️ Security Auditing:** Built-in tools for port scanning, network analysis, hash verification, and other white-hat security tasks.
- **🧹 Mole Cleaner:** Intelligently detects and removes unnecessary dummy files (cache, logs, temp) to optimize storage space.
- **🌐 AI Web Search:** Analyzes and summarizes web search results to deliver key information quickly.
- **🔒 Local First:** All tasks are performed locally, and depending on your AI model choice, it can operate in a completely offline environment.

---

## 🚀 Quick Install

Install or update instantly from your terminal without cloning or authentication:

```bash
pip install --upgrade git+https://github.com/hojinfreeacc-lgtm/hjc-claw.git
```

---

## 🧠 AI Setup

To enable intelligent features, set the environment variables for your preferred model.

### 1. Google Gemini (Recommended - Fast & Powerful)
```bash
export GOOGLE_API_KEY='your-gemini-api-key'
```

### 2. Local Google Gemma (Ollama - Secure & Offline)
```bash
export HJC_USE_OLLAMA='true'
export HJC_OLLAMA_MODEL='gemma2' # Options: gemma, llama3, etc.
```

### 3. OpenAI
```bash
export OPENAI_API_KEY='your-openai-api-key'
```

---

## 💻 Usage

After installation, simply type `hjc-claw` in your terminal.

### Example Commands
- **AI Tasks:** "Create a lotto number generator in Python and run it."
- **Web Search:** "Search for the latest AI news and summarize it."
- **Security:** "Scan my local ports," "Show network configuration."
- **System Cleanup:** "Run mole cleanup," "Analyze dummy files."
- **File Management:** "Find all .txt files and move them to the Documents folder."

---

## 🛠 Architecture

1. **Decision Engine:** A hybrid system combining rule-based matching and AI reasoning.
2. **Plugin Registry:** An extensible structure to easily add and manage new tools.
3. **Safe Executor:** A guardrail system that requests user approval before executing dangerous commands.
4. **Context Memory:** Remembers past commands and results for continuous task execution.

---

## 🔗 Links
- **GitHub:** [https://github.com/hojinfreeacc-lgtm/hjc-claw](https://github.com/hojinfreeacc-lgtm/hjc-claw)
- **License:** MIT License
