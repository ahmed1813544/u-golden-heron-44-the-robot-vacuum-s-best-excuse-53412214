"""The Robot Vacuum's Best Excuse.

Writes one line -- a deadpan excuse from a robot vacuum for missing
a spot -- to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
Stdlib only.
"""

import os

EXCUSE = (
    "My cliff sensor mistook the dark rug for a staircase, so I filed "
    "that spot under 'certain death' and went back to my dock."
)


def main():
    # Gate: entry.txt must be UTF-8 text of 1 to 140 characters.
    if not (1 <= len(EXCUSE) <= 140) or not EXCUSE.strip():
        raise SystemExit("excuse fails the 1-140 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
