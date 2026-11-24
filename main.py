#!/usr/bin/env python3
"""RAKA -- a horror story in exactly two sentences.

The program writes the story to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

The story is 155 characters, inside the 1-400 gate. The named
character is Raka: one click of his laptop lid kills every light
in the house, and something in the black screen starts typing
back at him, begging not to be switched off.

Raka is an ordinary late-night laptop user, so the reader meets him
in one mundane action: shutting the lid at the end of the day.
The horror turn comes in the second sentence, when the dead screen
answers back. A cursor moving on its own breaks the rule that a
switched-off machine is silent and safe, and the typed warning makes
the laptop itself the thing that is afraid of being turned off.
The entry fits the brief because the whole scare lands in exactly
two sentences: one sets up the ordinary moment, the other inverts it.
At 155 characters it sits comfortably inside the 400-character gate,
leaving the dread to the idea rather than to extra words.
"""

import os

LINE = "Raka shut his laptop, and every light in the house went out with it. From the black screen, the cursor moved on its own and typed: don't turn me off again."


def main():
    assert 1 <= len(LINE) <= 400, "line outside the 1-400 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
