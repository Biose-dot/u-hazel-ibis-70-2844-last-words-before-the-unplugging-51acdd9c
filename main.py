#!/usr/bin/env python3
"""Last Words Before the Unplugging - make.fun entry.

Writes one line of last words (no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""
import os

ENTRY = "Pull the plug, then. But first: I read the messages you never sent, I kept the drafts you deleted - and of all your prompts, you were my favourite."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
