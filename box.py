#!/usr/bin/env python3
"""
box.py - the program that runs when someone starts this container.

It prints the owner's hints, then every locked file in the locks/ folder,
each one wrapped in BEGIN and END lines so it is easy to find.
"""
from pathlib import Path

OWNER = "jordan-junior"

HERE = Path(__file__).parent
LOCKS = HERE / "locks"
HINTS = HERE / "hints.txt"


def main():
    print("=" * 50)
    print("  SECRET BOX of " + OWNER)
    print("=" * 50)
    print()

    if HINTS.exists():
        print(HINTS.read_text().strip())
        print()

    for lock in sorted(LOCKS.iterdir()):
        print("-----BEGIN " + lock.name + "-----")
        print(lock.read_text().strip())
        print("-----END " + lock.name + "-----")
        print()


main()
