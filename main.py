#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single sentence (at most 240 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, the file the sealed scorer reads.

Standard library only. No network, no randomness, no clock: the same
sentence is written on every run, byte for byte.
"""

import os
import sys

PITCH = (
    "You've carried that app idea for months \u2014 just tell an AI agent "
    "on make.fun in plain words and it will build you a working first "
    "version tonight, free to try, and you can change anything you "
    "don't like."
)


def main() -> int:
    if not 1 <= len(PITCH) <= 240:
        print(f"pitch is {len(PITCH)} characters, must be 1-240", file=sys.stderr)
        return 1
    if PITCH != PITCH.strip() or not PITCH:
        print("pitch must not be blank or padded", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH)
    # Read back what the grader will read: the file on disk must hold
    # exactly the pitch, or the run has failed even though the write
    # itself reported success.
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != PITCH:
        print("entry.txt on disk does not match the pitch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
