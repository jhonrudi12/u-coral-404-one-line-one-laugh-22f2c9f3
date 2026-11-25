#!/usr/bin/env python3
"""One Line, One Laugh — a single original joke line.

Writes one funny line to /output/entry.txt (or to the path given by
ENTRY_OUTPUT for local runs). The line is self-contained and checked
against the competition gate before it is written: UTF-8 text, 1 to
200 characters, non-blank, exactly one line.
"""

import os

LINE = (
    "My password manager forgot my password, so now we just stare at "
    "each other like two strangers at a family reunion."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_gate(text: str) -> None:
    """Check the competition gate: 1-200 chars, non-blank, one line, UTF-8."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text == text.strip(), "line must not start or end with whitespace"
    assert all(ord(ch) >= 0x20 for ch in text), "line must hold no control chars"
    text.encode("utf-8")


def main() -> None:
    text = LINE
    check_gate(text)

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
