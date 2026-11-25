#!/usr/bin/env python3
"""Invent a Word We Need - entry program.

Writes the coined word and its one-line definition to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only, no network.
"""

import os

ENTRY_TEXT = "canceljoy \u2014 the quiet delight when plans fall through and your evening is suddenly yours."

# The gate allows 1-140 characters, not only whitespace.
assert 1 <= len(ENTRY_TEXT) <= 140 and ENTRY_TEXT.strip(), "entry text outside the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    tmp_path = path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(ENTRY_TEXT.encode("utf-8"))
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
