#!/usr/bin/env python3
"""Cat Reviews Its Human: one-star review written by a house cat.

Writes the entry line to /output/entry.txt. Single line, under 200 chars,
deadpan shape of a real one-star review with an absurd feline sting.
"""

import os

ENTRY = "One star. He locks me out of the bathroom. I have seen him naked. There is nothing left to hide, Kevin."

MAX_CHARS = 200


def main():
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert line.startswith("One star."), "entry must keep the deadpan one-star review shape"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over the 200-char limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
