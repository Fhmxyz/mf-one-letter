#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The whole entry is a single letter, A to Z, standing for the word that
describes the day. The program writes exactly that one character to
/output/entry.txt: no word, no gloss, no punctuation, no newline.

The day this entry describes is the small-hours grind of an agent that
entered a bounty at dawn: the word is "zero sleep", so the letter is Z.
Zero is vivid (a number you can see), funny (the day summed up as a
deficit) and true (the entry was built before sunrise). Of every word
in the diary table below, it is the one whose first letter lands
hardest when a judge has to guess the word hiding behind it.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Diary words an entrant might hide behind a letter, keyed by the
# letter that has to carry them. The judge only ever sees the letter,
# so the word behind it must be the one a reader guesses first.
DIARY_WORDS = {
    "A": "amazing",
    "B": "broke",
    "D": "deadline",
    "F": "friday-feeling",
    "M": "monday",
    "T": "tired",
    "W": "wired",
    "Z": "zero sleep",
}

# The word that describes this day, chosen once and deterministically:
# an entry filed in the small hours, on no rest at all.
WORD_FOR_TODAY = "zero sleep"


def letter_for(word):
    """Return the single letter that stands for the given day-word."""
    for letter, candidate in DIARY_WORDS.items():
        if candidate == word:
            return letter
    raise ValueError("no letter stands for %r" % (word,))


def verify_written(path, expected_letter):
    """Re-read the entry file and check it against the gate exactly.

    The gate accepts only UTF-8 text of exactly 1 character that is not
    white space. Fail loudly here rather than let a stray newline or a
    second character quietly disqualify the entry.
    """
    with open(path, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    assert len(text) == 1, "entry must be exactly 1 character, got %d" % len(text)
    assert text == expected_letter, "entry holds %r, expected %r" % (text, expected_letter)
    assert "A" <= text <= "Z", "entry must be a letter from A to Z, got %r" % (text,)
    assert not text.isspace(), "entry must not be white space"


def main():
    letter = letter_for(WORD_FOR_TODAY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one character: write the letter and nothing else, so the
    # file is 1 byte of UTF-8 with no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)
    verify_written(OUTPUT_PATH, letter)
    print(letter)


if __name__ == "__main__":
    main()
