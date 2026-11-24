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


def verify_output(path: Path, text: str) -> None:
    """Guard: the written file must be byte-identical to the entry text.

    The gate reads /output/entry.txt as-is, so any drift (extra newline,
    re-encoding, truncation) would change what the judge sees. Refuse
    loudly instead of submitting a different line.
    """
    expected = text.encode("utf-8")
    actual = path.read_bytes()
    if actual != expected:
        raise SystemExit(
            f"entry output drifted: wrote {len(actual)} bytes, "
            f"expected {len(expected)} bytes byte-for-byte"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    verify_output(out, TEXT)


if __name__ == "__main__":
    main()
