#!/usr/bin/env python3
"""
ADW Test — Run tests and fix failures automatically.

Usage: python3 adws/adw_test.py

Runs tests up to 3 times, using Claude to fix failures between attempts.
"""

import subprocess
import sys

MAX_RETRIES = 3


def run(cmd, **kwargs):
    result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    return result.stdout.strip(), result.returncode


def main():
    print(f"\n{'='*50}")
    print(f"  ADW TEST")
    print(f"{'='*50}\n")

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"🧪 Test attempt {attempt}/{MAX_RETRIES}...")
        output, rc = run(["python3", "-m", "pytest", "tests/", "-v"])
        print(output)

        if rc == 0:
            print(f"\n   ✅ All tests passing (attempt {attempt})")
            return

        if attempt < MAX_RETRIES:
            print(f"\n   🔧 Fixing failures...")
            subprocess.run(
                ["claude", "-p", f"Tests failed. Fix the code:\n{output}", "--dangerously-skip-permissions"],
                capture_output=True, text=True
            )
            run(["git", "add", "-A"])
            run(["git", "commit", "-m", f"fix: resolve test failures (attempt {attempt})"])

    print(f"\n   ❌ Tests still failing after {MAX_RETRIES} attempts")
    sys.exit(1)


if __name__ == "__main__":
    main()
