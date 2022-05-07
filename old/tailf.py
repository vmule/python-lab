from __future__ import print_function
from collections import deque
import sys

class Tail(object):

  def __init__(self, path, lines=20):
    self.lines = lines
    self.path = path

  def print_lines(self, block_size=1024):

    f = open(self.path)
    f.seek(0,2)
    block_end_byte = f.tell()
    blocks = []
    wanted_lines = self.lines
    lines_to_go = self.lines

    while lines_to_go > 0 and block_end_byte > 0:
      if (block_end_byte - block_size > 0):
        f.seek(block_end_byte - block_size)
        blocks.append(f.read(block_size))

      else:
        f.seek(0)
        blocks.append(f.read(block_size))

      lines_found = blocks[-1].count('\n')
      lines_to_go -= lines_found
      block_end_byte -= block_size

    lines = ''.join(blocks[::-1])
    return '\n'.join(lines.splitlines()[-wanted_lines:])

  def print_lines2(self):
    with open(self.path) as f:
      lines = deque(f, self.lines)
    return lines


def main():
  instance = Tail(sys.argv[1])
  instance2 = Tail(sys.argv[1])
  print('Method 1')
  print(instance.print_lines())
  print()
  print('Method 2')
  lines = instance2.print_lines2()
  for line in lines:
    print(line, end='')

if __name__ == '__main__':
  main()
