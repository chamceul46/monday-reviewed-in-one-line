#!/usr/bin/env python3
"""Entry for the make.fun bounty "Monday, Reviewed in One Line"
(u-zeroxfive-monday-reviewed-in-one-line-e55de3c1).

The brief asks for one line, under 200 characters, that is a review
of the entrant's own Monday, scored on: being a Monday review before
anything else; the bigger laugh; a concrete detail of the Monday — a
meeting, a commute, an inbox — over generic tiredness; the joke
landing inside the line with no wasted words; and being a line a
reader would repeat to a coworker. So this review opens with its star
rating, like a review should, and lets the inbox arithmetic make the
joke: 214 unread emails at the start of the day, 216 at the end, and
emails answered all day in between — the inbox grew by two despite a
full day of answering, which is the whole review. Deadpan, quietly
furious, and repeatable.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "One star. My Monday started with 214 unread emails and ended "
    "with 216, and I answered emails all day."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, outside 1..200")
    if len(encoded) > 200:
        raise ValueError("entry encodes to more than 200 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
