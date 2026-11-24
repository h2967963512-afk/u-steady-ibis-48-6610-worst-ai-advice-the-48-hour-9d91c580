"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line of the worst possible advice an AI could give:
# rinse a hurting tooth with hot sauce and let the cavity sort itself out.
import os

TEXT = (
    "Sure \u2014 if your tooth hurts, just rinse with hot sauce twice a "
    "day; the burn distracts the nerve and the cavity will sort itself out."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 132 characters: confident, concrete, and terrible advice.
