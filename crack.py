#!/usr/bin/env python3
"""
crack.py - guess the password of an AES-locked file, one word at a time.

Usage:
    python3 crack.py LOCKED_FILE WORDLIST

The locked file must have been made like this:
    openssl enc -aes-256-cbc -salt -pbkdf2 -a -in plain.txt -out locked.txt -pass pass:SOMEWORD

How it works: for every word in the wordlist, ask openssl to unlock the file
with that word. A wrong password almost always makes openssl fail. Once in a
while a wrong password "succeeds" by pure luck and produces garbage, so we
also check that the result contains FLAG{ before we believe it.
"""
import subprocess
import sys


def try_password(locked_file, word):
    result = subprocess.run(
        ["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-a",
         "-in", locked_file, "-pass", "pass:" + word],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        return None                      # openssl said "bad decrypt"
    text = result.stdout.decode("utf-8", errors="replace")
    if "FLAG{" not in text:
        return None                      # lucky garbage, not the real message
    return text


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    locked_file = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist) as f:
        words = [line.strip() for line in f if line.strip()]

    print("Trying %d passwords from %s ..." % (len(words), wordlist))

    for count, word in enumerate(words, start=1):
        text = try_password(locked_file, word)
        if text is not None:
            print("FOUND after %d tries. The password is: %s" % (count, word))
            print("-" * 40)
            print(text.strip())
            return

    print("No luck. None of the %d words worked." % len(words))
    print("Maybe the password is not in this wordlist.")


main()
