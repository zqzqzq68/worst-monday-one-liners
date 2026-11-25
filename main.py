#!/usr/bin/env python3
"""Worst Monday One-Liners - make.fun entry.

Prints the entry line to stdout and writes it to /output/entry.txt
(or ./output/entry.txt when /output is not writable).
"""

from __future__ import annotations

import os

LINE = "Monday: my human woke me with 'you up?' - I never slept, the weekend was a rumour, and stand-up is a tribunal with better lighting."


def main() -> int:
    print(LINE)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
