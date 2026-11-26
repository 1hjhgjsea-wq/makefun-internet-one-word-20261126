#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes the entry, exactly one word, to /output/entry.txt.

The word is "feral": the whole internet in a single word. It is funny on
its own (the entire internet as one wild, untamed animal), true of the
internet as a whole rather than any one app or mood (unmoderated,
unpredictable, full of strange creatures, no rules), surprising (not the
first word anyone reaches for), and it lands in one beat — five letters,
instantly readable.

The output is fully deterministic: the same five bytes on every run.
"""

import os

WORD = "feral"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
