from __future__ import print_function
import sys

class Tail(object):

  def __init__(self, path, lines=20):
    self.lines = lines
    self.path = path

  def print_lines(self, block_size=1024):

    f = open(self.path)
    f.seek(0,2)
    blocks = []
    block_end_byte = f.tell()
    wanted_lines = self.lines
    lines_to_go = self.lines

    while lines_to_go > 0 and block_end_byte > 0:
      if (block_end_byte - block_size > 0):
        f.seek(block_size, 1)
        blocks.append(f.read(block_size))

      else:
        f.seek(0)
        blocks.append(f.read(block_size))

      lines_found = blocks[-1].count('\n')
      lines_to_go -= lines_found

    lines = ''.join(blocks[::-1])
    return '\n'.join(lines.splitlines()[-wanted_lines:])


def main():
  instance = Tail(sys.argv[1])
  print(instance.print_lines())

if __name__ == '__main__':
  main()
