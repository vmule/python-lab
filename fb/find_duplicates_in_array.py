import math

def findDuplicates(arr):
  # Write your code here
  
  seen_elements = {}
  for element in arr:
    if element in seen_elements:
      seen_elements[element] += 1
    else:
      seen_elements[element] = 1
  
  seen_too_much = []
  for key, value in seen_elements.items():
    if value > 1:
      seen_too_much.append(key)
      
  if len(seen_too_much) > 1:
    return sorted(seen_too_much)
  return []

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [0,3,1,2]
  expected_1 = []
  output_1 = findDuplicates(test_1)
  check(expected_1, output_1)
  
  test_2 = [2,3,1,2,3]
  expected_2 = [2,3]
  output_2 = findDuplicates(test_2)
  check(expected_2, output_2)

  test_3 = [1,2,3,4,7,5,4,3,2,1]
  expected_3 = [1,2,3,4]
  output_3 = findDuplicates(test_3)
  check(expected_3, output_3)
