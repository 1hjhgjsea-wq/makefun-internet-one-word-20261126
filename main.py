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
import sys

WORD = "feral"
OUTPUT_PATH = "/output/entry.txt"

# The entry gate: 1 to 30 UTF-8 characters, a single word, not only
# whitespace. Guard the word before writing, then read the file back
# and compare it to WORD so a bad write is never silent.
MIN_LENGTH = 1
MAX_LENGTH = 30


def validate_word(word: str) -> None:
    """Exit non-zero unless word is a single token within the gate's limits."""
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        print(
            f"error: entry length {len(word)} is outside "
            f"{MIN_LENGTH}-{MAX_LENGTH} characters",
            file=sys.stderr,
        )
        sys.exit(1)
    if word != word.strip() or any(ch.isspace() for ch in word):
        print("error: entry must be exactly one word, with no whitespace",
              file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(WORD.encode("utf-8"))
    # Verify the written file by reading it back and comparing it to WORD.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        print(
            f"error: verification failed — {OUTPUT_PATH!r} holds "
            f"{written!r}, expected {WORD.encode('utf-8')!r}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
