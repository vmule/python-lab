#!/usr/bin/env python
import sys

if __name__ == '__main__':
  string = sys.stdin.readlines()[0].strip()
  if string == string[::-1] :
      print string
