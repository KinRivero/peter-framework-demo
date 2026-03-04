#!/usr/bin/env python3
"""
ADW Review — Automated code review against main branch.

Usage: python3 adws/adw_review.py
"""

import subprocess
import sys


def main():
    print(f"\n{'='*50}")
    print(f"  ADW REVIEW")
    print(f"{'='*50}\n")

    print("🔍 Reviewing changes against main...")
    result = subprocess.run(
        ["claude", "-p", "/review", "--dangerously-skip-permissions"],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        print("   ✅ Review complete")
    else:
        print(f"   ⚠️ Review encountered issues")

    print(f"\n{'='*50}")
    print(f"  ✅ REVIEW COMPLETE")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
