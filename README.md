# Calculator API — PETER Framework Demo

> **"An issue goes in. A PR comes out. You were at lunch."**

A production-ready Python calculator with REST API, demonstrating the **PETER Framework** for autonomous AI Developer Workflows (ADWs).

## 🎯 What This Demonstrates

The PETER framework for building autonomous engineering pipelines:

| Element | Description | In This Repo |
|---------|-------------|--------------|
| **P**rompt input | Work request | GitHub Issues |
| **E**nvironment | Execution space | This repo + git worktrees |
| **T**rigger | What starts it | `adws/adw_sdlc.py` |
| **R**eview | Validation gate | Pull Requests |

## 🚀 Quick Start

```bash
# Install deps
pip install -r requirements.txt

# Run tests
python3 -m pytest tests/ -v

# Start API
python3 -m uvicorn src.api:app --reload --port 8000

# Try it
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"a": 2, "b": 3}'
```

## 🤖 ADW Pipeline (Autonomous SDLC)

Run the full pipeline on any GitHub issue:

```bash
python3 adws/adw_sdlc.py <issue-number>
```

What happens:
1. **Plan** — Fetches issue, classifies (chore/bug/feature), generates spec
2. **Build** — Implements from the spec using Claude Code
3. **Test** — Runs tests, fixes failures automatically
4. **Review** — Code quality check
5. **PR** — Creates pull request for human review

**Zero human intervention during execution.** You review the PR when it's done.

## 📁 Project Structure

```
peter-framework-demo/
├── CLAUDE.md                    # Agent instructions
├── src/
│   ├── calculator.py            # Core math functions
│   └── api.py                   # FastAPI REST API
├── tests/
│   ├── test_calculator.py       # Unit tests
│   └── test_api.py              # API integration tests
├── adws/                        # AI Developer Workflows
│   ├── adw_plan.py              # Planning agent
│   ├── adw_build.py             # Build agent
│   ├── adw_test.py              # Test agent
│   ├── adw_review.py            # Review agent
│   └── adw_sdlc.py              # Full SDLC pipeline
├── .claude/commands/            # Slash command templates
│   ├── classify_issue.md
│   ├── feature.md
│   ├── implement.md
│   ├── review.md
│   ├── chore.md
│   └── bug.md
├── specs/                       # Generated implementation plans
├── requirements.txt
└── scripts/
    └── start.sh
```

## 📊 KPIs

| KPI | Direction | What it measures |
|-----|-----------|-----------------|
| Presence ↓ | Less time babysitting | You're reviewing, not writing |
| Size ↑ | Bigger tasks delegated | Agents handle complex work |
| Streak ↑ | Consecutive successes | System is reliable |
| Attempts ↓ | Fewer retries needed | One-shot success |

## Source

Based on [Tactical Agentic Coding (TAC)](https://agenticengineer.com) by IndyDevDan — Lessons 4-7.
