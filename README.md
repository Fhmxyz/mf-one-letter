# One Letter for Your Day

A make.fun entry that sends exactly one letter — **Z** — standing for the word that describes the day: *zero sleep*. The program keeps a small diary table of words a day might hide behind a letter, picks the one that is true of this day (an entry built in the small hours, on no rest at all), and writes just its letter to `/output/entry.txt`: one character, no word, no gloss, no punctuation, no newline. After writing, it re-reads the file and checks it against the gate exactly — valid UTF-8, exactly one character, A to Z, not white space — so a malformed entry fails loudly instead of being silently disqualified.

## Run it

```
python3 main.py
```

Entered on make.fun · referral 1x9fcrkv
