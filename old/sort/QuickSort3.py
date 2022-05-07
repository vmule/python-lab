def quicksort3(list_, start=0, end=-1):
  if end == -1:
      end = len(list_)
  if start < end-1:
    i =  start
    j = end
    pivot = list_[start]
    k = start+1
    while(k < j):
      while(pivot < list_[k]):
        j -= 1
        tmp = list_[k]
        list_[k] = list_[j]
        list_[j] = tmp
      if list_[k] < pivot:
        tmp = list_[k]
        list_[k] = list_[i]
        list_[i] = tmp
        i += 1
      k +=1
    quicksort3(list_, start, i)
    quicksort3(list_, j, end)

list_ = [31,0,45,2,23,9,21,54,99,32,4,8,5]
print(list_)
quicksort3(list_)
print(list_)
