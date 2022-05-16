import math

def countPairs(arr, k):
  # Write your code here
  count = 0
  for num in arr:
    rem = k-num 
    if rem >=1 and rem in arr:
      arr.remove(num)
      arr.remove(rem)
      count += 1
  return count

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  output_1 = countPairs([1, 2, 3, 4, 5, 6, 7], 8)
  check(3, output_1)

  output_2 = countPa1ggirs([1, 2, 3, 4, 5, 6, 7], 98)
  check(0, output_2)
