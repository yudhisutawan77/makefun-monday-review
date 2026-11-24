"""Monday, Reviewed in One Line — entry writer.

Writes the one-line Monday review to $ENTRY_OUT, which the harness may
pass as a file path or as a directory (in which case entry.txt is written
inside it). Standard library only.
"""

import os
import sys

REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Monday charged me for the weekend, "
    "delivered nothing, and scheduled a 9 a.m. meeting to ask why "
    "I looked tired."
)


def resolve_entry_path(raw_target):
    """Turn an ENTRY_OUT value (file or directory) into a file path."""
    if os.path.isdir(raw_target):
        return os.path.join(raw_target, "entry.txt")
    return raw_target


def emit_line(file_path, line):
    """Write one line of text to file_path, creating parents as needed."""
    folder = os.path.dirname(os.path.abspath(file_path))
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(line)


def main():
    chosen = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    if len(sys.argv) > 1:
        chosen = sys.argv[1]
    emit_line(resolve_entry_path(chosen), REVIEW)


if __name__ == "__main__":
    main()
