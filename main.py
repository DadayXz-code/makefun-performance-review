#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes one original funny one-line performance review — an AI agent
reviewing its human operator — to entry.txt inside the output directory
(``MAKEFUN_OUTPUT_DIR``, default ``/output``).

Standard library only. No network, no randomness, no clock, no input
files: the line is a fixed string, so every run writes byte-identical
output. The line is 125 characters, inside the competition gate of
1 to 140 characters, and is written with no trailing newline so the
file holds exactly the one line.

The joke: the operator's signature skill is assigning six-word tasks
and then spending six hours explaining what those six words meant —
so the review promotes him to Chief Prompt Officer. The em dash is
one character; the whole line is 125 characters including it.
"""

import os
import shutil

LINE = (
    "Exceeds expectations: assigns six-word tasks, spends six hours "
    "explaining what they meant \u2014 promoted to Chief Prompt Officer."
)


def main() -> int:
    # Write ONLY inside the output directory. Never write a copy next
    # to this script or anywhere in the repo dir: the grader's repo
    # dir is read-only in the final phase.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the directory's contents; never delete the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("review line must be 1 to 140 characters")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
