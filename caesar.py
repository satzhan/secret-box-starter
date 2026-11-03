#!/usr/bin/env python3
"""
caesar.py - slide every letter of a text forward by a fixed number of places.

    A B C D E ...      with a shift of 3 becomes      D E F G H ...

Usage:
    python3 caesar.py encrypt SHIFT FILE    print the locked version of FILE
    python3 caesar.py decrypt SHIFT FILE    print the unlocked version of FILE
    python3 caesar.py crack FILE            try every shift, print all of them

Only letters move. Digits, spaces, braces and dashes stay where they are.
"""
import sys


def shift_text(text, shift):
    result = []
    for ch in text:
        if "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        else:
            result.append(ch)
    return "".join(result)


def read_file(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "encrypt" and len(sys.argv) == 4:
        shift = int(sys.argv[2])
        print(shift_text(read_file(sys.argv[3]), shift), end="")

    elif command == "decrypt" and len(sys.argv) == 4:
        shift = int(sys.argv[2])
        print(shift_text(read_file(sys.argv[3]), -shift), end="")

    elif command == "crack" and len(sys.argv) == 3:
        locked = read_file(sys.argv[2])
        # There are only 26 possible shifts, so just try them all.
        for shift in range(26):
            for line in shift_text(locked, -shift).splitlines():
                print("[shift %2d] %s" % (shift, line))

    else:
        print(__doc__)
        sys.exit(1)


main()
