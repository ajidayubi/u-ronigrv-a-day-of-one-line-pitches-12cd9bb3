#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun bounty entry.

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun.
"""

import os

SENTENCE = (
    "If you've never written a line of code, just describe your app idea "
    "in plain words on make.fun and an AI agent builds it for you "
    "\u2014 your idea, its code, your first real app."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
