class Node:

  def __init__(self, key, data):
    self.key = key
    self.data = data
    self.next = None
    self.prev = None


class LRUCache:

  def __init__(self, capacity):
    self.capacity = capacity
    self.map = {}
    self.head = None
    self.tail = None
    
  def __str__(self):
    _llist = []
    temp_pointer_node = self.head
    while temp_pointer_node:
        _llist.append((temp_pointer_node.key, temp_pointer_node.data))
        temp_pointer_node = temp_pointer_node.next
    if len(_llist) > 0:
        return ' '.join(str(i) for i in _llist)
    return '[ ]'

  def append_node(self, node):
    if not self.tail:
      self.head = self.tail = node
      return
    
    if node is self.tail:
      return
    
    self.tail.next = node
    node.prev = self.tail
    self.tail = node

  def unlink_node(self, node):
    if node is self.head:
      self.head = node.next
      if self.head:
        self.head.prev = None
      return
    if node is self.tail:
      self.tail = node.prev
      if self.tail:
        self.tail.next = None
    return
    node.prev.next = node.next
    node.next.prev = node.prev

  def get(self, key):
    if key not in self.map:
      return -1
    node = self.map[key]

    self.unlink_node(node)
    self.append_node(node)
    return node.data

  def set(self, key, data):
    if key in self.map:
      node = self.map[key]
      node.data = data
      self.get(data)
      return

    if len(self.map) >= self.capacity:
      if self.capacity == 1:
        self.map = {}
        self.head = None
        self.tail = None
      else:
        _key = self.head.key
        self.map.pop(_key)
        self.unlink_node(self.head)

    new_node = Node(key, data)
    self.map[key] = new_node
    self.append_node(new_node)
    return
      

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
  cacheOne = LRUCache(2) 
  cacheOne.set(1, 2)
  outputOne = [cacheOne.get(1)]
  check([2], outputOne)

  cacheTwo = LRUCache(2)
  cacheTwo.set(1,2)
  cacheTwo.set(2,3)
  cacheTwo.set(1,5)
  cacheTwo.set(4,5)
  cacheTwo.set(6,7)
  outputTwo = [cacheTwo.get(4)]
  cacheTwo.set(1,2)
  outputTwo.append(cacheTwo.get(3))
  check([5, -1], outputTwo)
