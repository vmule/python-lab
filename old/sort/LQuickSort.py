"""http://stackoverflow.com/questions/12107790/python-quicksort-list-comprehension-vs-recursion-partition-routine"""


def sort(xs):
  if xs == []:
    return []
  pivot = xs[0]
  as_ = sort([x for x in xs[0] if x < pivot])
  bs = sort([x for x in xs[0] if x >= pivot])
  return as_ + [pivot] + bs


list = [3,0,45,2,23,9,21,54,99,32,4,8,5]
a = sort(list)
print(a)

