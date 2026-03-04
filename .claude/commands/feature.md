# Feature Planning

Create a plan to implement the feature described in the GitHub issue.

## Variables
issue_number: $1
issue_title: $2
issue_body: $3

## Instructions
- Research the codebase (read CLAUDE.md, src/, tests/)
- Create a plan in `specs/issue-{issue_number}-{descriptive-name}.md`
- Use this format:

### Plan Format
```markdown
# Issue #{issue_number}: {title}

## Summary
Brief description of what will be implemented.

## Relevant Files
- List existing files that will be modified
- List new files that will be created

## Step by Step Tasks
1. [ ] Task 1 — description
2. [ ] Task 2 — description  
3. [ ] Task 3 — description

## Validation Commands
- `python3 -m pytest tests/ -v` — all tests pass

## Notes
- Edge cases to handle
- Design decisions
```

- Follow existing patterns in the codebase
- Include test tasks for every new function
- Return ONLY the path to the created spec file
