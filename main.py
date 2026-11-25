"""Real-Life Patch Notes entry: write one comedy changelog line.

The entry is a single-line software patch note for a bug in human
biology, written in the terse register of a real release note. The
program validates the line against the competition gate (UTF-8 text,
1 to 160 characters, a single non-blank line) and writes it to
/output/entry.txt, readable by the grader.
"""

import os

ENTRY = (
    "v3.2.1: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2009 every night at 3 a.m."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate(text):
    """Check one candidate line against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError("entry must be 1 to 160 characters")
    text.encode("utf-8")
    return text


def main():
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
