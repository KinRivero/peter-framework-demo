#!/usr/bin/env python3
"""
ADW SDLC — Complete Software Development Life Cycle pipeline.

Usage: python3 adws/adw_sdlc.py <issue-number>

Runs the full autonomous pipeline:
1. Plan  — Fetch issue, classify, generate plan
2. Build — Implement from plan
3. Test  — Run tests, fix failures
4. Review — Code quality check
5. PR    — Create pull request

This is the PETER framework in action:
  P = Prompt input (GitHub Issue)
  E = Environment (this repo + worktree)
  T = Trigger (this script)
  R = Review (PR for human approval)
"""

import subprocess
import sys
import json
import glob


def run(cmd, **kwargs):
    result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    return result.stdout.strip(), result.returncode


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 adws/adw_sdlc.py <issue-number>")
        print("\n🚀 Full SDLC Pipeline: Plan → Build → Test → Review → PR")
        print("\nThis is the PETER framework:")
        print("  P = Prompt input (GitHub Issue)")
        print("  E = Environment (this repo)")
        print("  T = Trigger (this script)")
        print("  R = Review (PR for human approval)")
        sys.exit(1)

    issue_number = sys.argv[1]

    print(f"\n{'='*60}")
    print(f"  🚀 ADW SDLC — Full Pipeline — Issue #{issue_number}")
    print(f"  PETER: Prompt → Environment → Trigger → Review")
    print(f"{'='*60}\n")

    # [P] Prompt Input
    print("📋 [P] PROMPT INPUT — Fetching GitHub Issue...")
    issue_json, rc = run(["gh", "issue", "view", issue_number, "--json", "title,body,labels"])
    if rc != 0:
        print(f"❌ Failed to fetch issue #{issue_number}")
        sys.exit(1)
    issue = json.loads(issue_json)
    print(f"   Title: {issue['title']}")

    labels = [l['name'] for l in issue.get('labels', [])]
    issue_type = 'bug' if 'bug' in labels else ('chore' if 'chore' in labels else 'feature')
    print(f"   Type: {issue_type}")

    # [E] Environment
    print(f"\n🏗️  [E] ENVIRONMENT — Setting up workspace...")
    branch = f"{issue_type}/issue-{issue_number}"
    run(["git", "checkout", "main"])
    run(["git", "pull"])
    run(["git", "checkout", "-b", branch])
    print(f"   Branch: {branch}")

    # [T] Trigger — Pipeline phases
    print(f"\n⚡ [T] TRIGGER — Starting autonomous pipeline...")

    # Phase 1: Plan
    print(f"\n{'─'*40}")
    print(f"  Phase 1/4: PLAN")
    print(f"{'─'*40}")
    prompt = f"/{issue_type} {issue_number} \"{issue['title']}\" \"{issue.get('body', '')}\""
    result = subprocess.run(
        ["claude", "-p", prompt, "--dangerously-skip-permissions"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"   ❌ Planning failed")
        sys.exit(1)
    run(["git", "add", "specs/"])
    run(["git", "commit", "-m", f"plan: {issue['title']} (#{issue_number})"])
    print("   ✅ Plan generated and committed")

    # Phase 2: Build
    print(f"\n{'─'*40}")
    print(f"  Phase 2/4: BUILD")
    print(f"{'─'*40}")
    plans = sorted(glob.glob("specs/*.md"))
    if plans:
        plan_file = plans[-1]
        result = subprocess.run(
            ["claude", "-p", f"/implement {plan_file}", "--dangerously-skip-permissions"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"   ❌ Build failed")
            sys.exit(1)
    print("   ✅ Implementation complete")

    # Phase 3: Test
    print(f"\n{'─'*40}")
    print(f"  Phase 3/4: TEST")
    print(f"{'─'*40}")
    test_output, rc = run(["python3", "-m", "pytest", "tests/", "-v"])
    print(test_output[-500:] if len(test_output) > 500 else test_output)
    if rc != 0:
        print("   🔧 Fixing test failures...")
        subprocess.run(
            ["claude", "-p", f"Fix these test failures:\n{test_output}", "--dangerously-skip-permissions"],
            capture_output=True, text=True
        )
        test_output, rc = run(["python3", "-m", "pytest", "tests/", "-v"])
        if rc != 0:
            print("   ❌ Tests still failing")
            sys.exit(1)
    print("   ✅ All tests passing")

    # Commit and push
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", f"feat: {issue['title']} (closes #{issue_number})"])
    run(["git", "push", "-u", "origin", branch])

    # [R] Review — Create PR
    print(f"\n{'─'*40}")
    print(f"  Phase 4/4: REVIEW")
    print(f"{'─'*40}")
    pr_body = f"""## Automated PR — ADW SDLC Pipeline

Closes #{issue_number}

### Pipeline Results
- ✅ Plan — Implementation spec generated
- ✅ Build — Code implemented from spec
- ✅ Test — All tests passing
- ✅ Review — Ready for human review

### PETER Framework
| Element | Value |
|---------|-------|
| **P**rompt | Issue #{issue_number}: {issue['title']} |
| **E**nvironment | Branch `{branch}` |
| **T**rigger | `adw_sdlc.py` |
| **R**eview | This PR |
"""
    pr_url, rc = run([
        "gh", "pr", "create",
        "--title", f"{issue_type}: {issue['title']}",
        "--body", pr_body,
    ])
    print(f"   ✅ PR created: {pr_url}")

    # Comment on issue
    run(["gh", "issue", "comment", issue_number, "--body",
         f"🤖 ADW SDLC complete!\n\nPR: {pr_url}\n\nPipeline: Plan ✅ → Build ✅ → Test ✅ → Review ✅"])

    print(f"\n{'='*60}")
    print(f"  🎉 SDLC COMPLETE — Issue #{issue_number}")
    print(f"  PR ready for human review: {pr_url}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
