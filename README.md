# PETER Framework Demo

> "An issue goes in. A PR comes out. You were at lunch."

A minimal Python project demonstrating the **PETER Framework** for autonomous AI Developer Workflows (ADWs).

## What is PETER?

| Element | Description |
|---------|-------------|
| **P**rompt input | GitHub Issue — title, body, labels |
| **E**nvironment | Isolated execution space for agents |
| **T**rigger | Webhook, cron, or manual script |
| **R**eview | Pull Request — approval gate before merge |

## The Flow

```
GitHub Issue → Classifier → Branch → Plan → Build → Test → PR
```

Zero human intervention. The complete SDLC runs autonomously.

## Project Structure

```
peter-demo/
├── src/
│   └── calculator.py      # Simple calculator module
├── tests/
│   └── test_calculator.py  # Test suite
├── requirements.txt
└── README.md
```

## Try It

```bash
# Run tests
python -m pytest tests/ -v

# Create a GitHub issue, then watch the magic happen
```

## KPIs

| KPI | Direction | Target |
|-----|-----------|--------|
| Presence | ↓ | <10% time in-loop |
| Size | ↑ | >500 LOC per task |
| Streak | ↑ | 20+ consecutive wins |
| Attempts | ↓ | <1.5 average |

## Source

Based on [Tactical Agentic Coding (TAC)](https://agenticengineer.com) by IndyDevDan.
