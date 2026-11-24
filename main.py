"""One line: the cat joke that lands.

Writes one sentence to /output/entry.txt: the owner does everything
(rent, food, litter) and the cat still treats them like the intern.
Setup plus turn, no tired cat pun: the joke is a status reversal,
workplace hierarchy applied to the cat-owner relationship.
"""

from pathlib import Path

TEXT = (
    "I pay the rent, buy the food, and scoop the litter \u2014 and my "
    "cat still looks at me like I'm the intern."
)


# The competition accepts texts of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
