#!/usr/bin/env python3
"""
ADW Build — Implement from a plan file.

Usage: python3 adws/adw_build.py [plan-file]

This agent:
1. Reads the plan from specs/
2. Implements each task using Claude Code
3. Runs tests to verify
4. Commits implementation
"""

import subprocess
import sys
import glob


def run(cmd, **kwargs):
    result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    return result.stdout.strip(), result.returncode


def main():
    if len(sys.argv) < 2:
        plans = sorted(glob.glob("specs/*.md"))
        if not plans:
            print("Usage: python3 adws/adw_build.py <plan-file>")
            sys.exit(1)
        plan_file = plans[-1]
    else:
        plan_file = sys.argv[1]

    print(f"\n{'='*50}")
    print(f"  ADW BUILD — {plan_file}")
    print(f"{'='*50}\n")

    # Step 1: Implement
    print("🔨 Implementing from plan...")
    result = subprocess.run(
        ["claude", "-p", f"/implement {plan_file}", "--dangerously-skip-permissions"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"   ❌ Build failed")
        sys.exit(1)
    print("   ✅ Implementation complete")

    # Step 2: Test
    print("\n🧪 Running tests...")
    test_output, rc = run(["python3", "-m", "pytest", "tests/", "-v"])
    print(test_output)
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

    # Step 3: Commit
    print("\n💾 Committing...")
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", f"feat: implement {plan_file}"])
    run(["git", "push"])
    print("   ✅ Committed and pushed")

    print(f"\n{'='*50}")
    print(f"  ✅ BUILD COMPLETE")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
