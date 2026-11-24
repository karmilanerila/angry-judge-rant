"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant about an everyday annoyance to entry.txt in the
output directory. The rant is baked into this file: the program has no
inputs, no network, and no dependencies beyond the standard library.
"""

import os

RANT = (
    "My smoke alarm has never chirped at noon. Not once. "
    "It waits until 3 a.m., beeps a single time, then goes silent for an "
    "hour so I lie there wondering if I dreamed it. Last night I stood on "
    "a chair in the dark, holding a broom, negotiating with a plastic disc "
    "on my ceiling. The disc won. It is still up there, fully charged "
    "with contempt."
)


def output_path() -> str:
    """Return the path entry.txt should be written to."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> None:
    text = RANT.strip()
    if not text:
        raise SystemExit("rant is empty")
    if not 1 <= len(text) <= 400:
        raise SystemExit(f"rant is {len(text)} chars, must be 1-400")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
