def partition(list_, l, r):
  p_idx = l
  for i in range(l+1, r):
    if list_[p_idx] > list_[i]:
      l += 1
      tmp = list_[l]
      list_[l] = list_[i]
      list_[i] = tmp
    else:
      pass
  tmp = list_[p_idx]
  list_[p_idx] = list_[l]
  list_[l] = tmp
  return l + 1

def quicksort(list_, l, u):
  if l < u:
    m = partition(list_, l, u)
    quicksort(list_, l, m-1)
    quicksort(list_, m, u)
list_ = [31,0,45,2,23,9,21,54,99,32,4,8,5]
print(list_)
quicksort(list_, 0, len(list_))
print(list_)
