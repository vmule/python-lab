def getTrappedRainWater(arr):
  blocks = 0
  pillar = 0
  i = 0
  while pillar < len(arr) and i+1 < len(arr):
    if (arr[pillar] >= 1) and (arr[pillar] - arr[i+1]) >= 0:
      blocks = blocks + (arr[pillar] - arr[i+1])
      i = i + 1
    else:
      i = i + 1
      pillar = i
  return blocks

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  outputOne = getTrappedRainWater([7,4,0,9]);
  check(10, outputOne);
  outputTwo = getTrappedRainWater([6,9,9]);
  check(0, outputTwo)
  # Add your own test cases here
  outputThree = getTrappedRainWater([1,9,0,0,0,0,9,2,9]);
  check(43, outputThree)
  outputFour = getTrappedRainWater([1,0,0,0,0,9,0,9]);
  check(13, outputFour)
  outputFive = getTrappedRainWater([4,2,0,3,2,5]);
  check(9, outputFive)
