#!/usr/bin/env python

class Palindromes:
  def __init__(self, string):
    self.string = string
    print self.string
    self.palindromes_set = set()

  def findPalindromes(self):
    for idx, char in  enumerate(self.string):

      self.palindromes_set.add(self.string[idx])
      start = idx - 1
      end = idx + 1
      while start >= 0 and end < len(self.string)  and  self.string[start] == self.string[end]:
        self.palindromes_set.add(self.string[start:end+1])
        start -= 1
        end += 1

      start = idx
      end = idx + 1
      while start >= 0 and end < len(self.string) and  self.string[start] == self.string[end]:
        self.palindromes_set.add(self.string[start:end+1])
        start -= 1
        end += 1

    return list(self.palindromes_set)

def main(string):
  p = Palindromes(string)
  print p.findPalindromes()

if __name__ == '__main__':
  main('accaaccasasdfasdfqwretawfphqwefpoqwefqhfdfhdhdhhhffdygdfkdsafdfh')

