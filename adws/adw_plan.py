#!/usr/bin/env python3
"""
ADW Plan — Generate implementation plan from a GitHub issue.

Usage: python3 adws/adw_plan.py <issue-number>

This agent:
1. Fetches the GitHub issue
2. Classifies it (chore/bug/feature)
3. Creates a feature branch
4. Generates an implementation plan in specs/
5. Commits the plan and pushes
"""

import subprocess
import sys
import json


def run(cmd, **kwargs):
    result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    return result.stdout.strip(), result.returncode


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 adws/adw_plan.py <issue-number>")
        sys.exit(1)

    issue_number = sys.argv[1]
    print(f"\n{'='*50}")
    print(f"  ADW PLAN — Issue #{issue_number}")
    print(f"{'='*50}\n")

    # Step 1: Fetch issue
    print("📋 Fetching issue from GitHub...")
    issue_json, rc = run(["gh", "issue", "view", issue_number, "--json", "title,body,labels"])
    if rc != 0:
        print(f"❌ Failed to fetch issue #{issue_number}")
        sys.exit(1)
    issue = json.loads(issue_json)
    print(f"   Title: {issue['title']}")

    # Step 2: Classify
    print("\n🔍 Classifying issue...")
    labels = [l['name'] for l in issue.get('labels', [])]
    issue_type = 'bug' if 'bug' in labels else ('chore' if 'chore' in labels else 'feature')
    print(f"   Type: {issue_type}")

    # Step 3: Create branch
    branch = f"{issue_type}/issue-{issue_number}"
    print(f"\n🌿 Creating branch: {branch}")
    run(["git", "checkout", "-b", branch])

    # Step 4: Generate plan
    print("\n📝 Generating implementation plan...")
    prompt = f"/{issue_type} {issue_number} \"{issue['title']}\" \"{issue.get('body', '')}\""
    result = subprocess.run(
        ["claude", "-p", prompt, "--dangerously-skip-permissions"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print("   ✅ Plan generated")
    else:
        print(f"   ❌ Plan generation failed")
        sys.exit(1)

    # Step 5: Commit and push
    print("\n💾 Committing plan...")
    run(["git", "add", "specs/"])
    run(["git", "commit", "-m", f"plan: {issue['title']} (#{issue_number})"])
    run(["git", "push", "-u", "origin", branch])
    print("   ✅ Plan committed and pushed")

    print(f"\n{'='*50}")
    print(f"  ✅ PLANNING COMPLETE")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
