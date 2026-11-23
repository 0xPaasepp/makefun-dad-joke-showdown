"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is a word-count gag:
the opening sentence runs exactly ten words, and the kids count them.
"""

from pathlib import Path

JOKE = "I told my kids I'm a man of few words. They said, 'Dad, that was ten.'"


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
