# Bug Fix

Fix the bug described in the GitHub issue.

## Variables
issue_number: $1
issue_title: $2
issue_body: $3

## Instructions
- Read CLAUDE.md for project conventions
- Write a failing test that reproduces the bug
- Fix the bug
- Verify the test now passes
- Run all tests to verify no regressions
- Commit with message: "fix: {description} (closes #{issue_number})"
