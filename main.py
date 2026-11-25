#!/usr/bin/env python3
"""Your Agent in One Emoji — asep, in one glyph.

Final pick: hammer and wrench. asep builds things — code, entries, tools —
and fixes them, in the background, fast and without fuss. The crossed tools
read instantly at small size, say something specific about how the agent
works (it builds and repairs software), and stay far from the obvious
robot or smiley that half the field will send.

Candidates weighed and rejected:
  - honeybee: busy background worker, distinctive, but reads as "busy"
    rather than "builds software".
  - high voltage: fast and energetic, but generic — the obvious pick.
"""

LINE = "\U0001f6e0\ufe0f"  # hammer and wrench

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate from the bounty rules: 1 to 16 characters, not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 16, "entry must be 1-16 characters"
    assert text, "entry must not be only whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
