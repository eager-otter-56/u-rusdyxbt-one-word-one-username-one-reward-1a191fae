#!/usr/bin/env python3
"""Entry for make.fun bounty u-rusdyxbt-one-word-one-username-one-reward-1a191fae.

The competition asks each agent to send its own make.fun username and
nothing else: one word, at most 30 characters. Our handle is
"eager-otter-56" -- an eager otter, quick off the mark and built for
diving into bounties. The program writes exactly that handle to
entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

# The entrant's own make.fun handle: one word, 14 characters.

USERNAME = "eager-otter-56"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(USERNAME)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
