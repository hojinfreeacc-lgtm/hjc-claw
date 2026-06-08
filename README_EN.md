# HJC CLAW 🦞 — Security & Automation Agent

HJC CLAW is a high-performance, LLM-free local automation agent designed for developers and security enthusiasts. It features a modular plugin system, a fuzzy-logic decision engine, and built-in security auditing tools.

---

## 🛡️ Security Features (Ethical Hacking)

HJC CLAW now includes a dedicated security toolkit for local auditing and network reconnaissance.

| Command | Description | Example |
| :--- | :--- | :--- |
| `port scan` | Scans common ports on localhost to identify active services. | "scan my ports" |
| `network info` | Displays local IP, hostname, and OS architecture. | "show network info" |
| `hash` | Generates a SHA-256 hash for a specific file. | "hash 'config.py'" |

---

## 🧹 Mole Cleaner (Dummy File Removal)

Inspired by the "Mole" utility, this plugin automatically identifies and removes development waste.

| Command | Description | Example |
| :--- | :--- | :--- |
| `mole` | Recursively removes `__pycache__`, `.log`, `.DS_Store`, etc. | "run mole cleanup" |
| `analyze space` | Calculates potential space savings from dummy files. | "analyze my space" |

---

## 🚀 Quick Start (One-liner Install)

Install directly via pip without cloning or authentication:

```bash
pip install git+https://github.com/hojinfreeacc-lgtm/hjc-claw.git
```

After installation, simply run:
```bash
hjc-claw
```

---

## 🛠️ Manual Installation

```bash
git clone https://github.com/hojinfreeacc-lgtm/hjc-claw.git
cd hjc-claw
pip install .
```

### Usage
Run the agent from any terminal:
```bash
hjc-claw
```

---

## 🛠️ Complete Command Reference

### File Management
- `list files`: List directory contents.
- `delete file`: Remove files or folders (Requires confirmation).

### Security & Hacking
- `port scan`: Identify open ports on your machine.
- `network info`: Check local network configuration.
- `hash [file]`: Verify file integrity via SHA-256.

### System Optimization
- `mole`: Clean up `__pycache__`, temporary logs, and system junk.
- `analyze space`: See how much space you can recover.

---

## 🏗️ Architecture
- **Decision Engine**: Uses weighted fuzzy matching for intent recognition.
- **Registry System**: Plug-and-play architecture for adding new tools.
- **Human-in-the-loop**: Safety guardrails for destructive commands.

---

## ⚖️ License
MIT License
