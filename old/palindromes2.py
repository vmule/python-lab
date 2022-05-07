#!/usr/bin/env python
import sys


def palindromes(text):
    text = text.lower()
    results = set()

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results.add(chunk)

    return results


def main(string):
    print palindromes(string)

if __name__ == '__main__':
    string = sys.stdin.readlines()[0]
    main(string.strip())
