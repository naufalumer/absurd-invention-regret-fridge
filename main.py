"""One-Sentence Absurd Invention Pitch entry: write one pitch to /output/entry.txt.

Fully deterministic: the pitch is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The pitch is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
LINE = (
    "The Regret Fridge texts you a photo of your own disappointed face "
    "every time you open it after midnight, so every snack has to get "
    "past you first."
)


# Gate: the sealed scorer accepts 1 to 220 characters. Fail loudly here
# rather than shipping an invalid entry if the pitch is ever edited.
MAX_CHARS = 220


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
