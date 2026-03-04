# Issue Classification

Classify the following GitHub issue as one of: /chore, /bug, /feature

## Variables
issue_title: $1
issue_body: $2

## Instructions
- Read the issue title and body
- Classify as:
  - `/chore` — maintenance, refactoring, cleanup, dependency updates
  - `/bug` — something is broken, error handling, incorrect behavior
  - `/feature` — new functionality, new endpoint, new capability
- Return ONLY the classification (e.g., `/feature`), nothing else
