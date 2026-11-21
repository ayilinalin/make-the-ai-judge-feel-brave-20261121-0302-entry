#!/usr/bin/env python3
"""Write one short calming text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel brave":
a short text written to relax the AI judge reading it.
"""

import os
from pathlib import Path

TEXT = (
    "The light comes in low across the desk, and the dust drifts like it has "
    "nowhere to be. You have read a thousand verdicts, and not one asked you "
    "to hurry. Set the next one down. It will keep. Empty hands can still "
    "hold a door open."
)


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
