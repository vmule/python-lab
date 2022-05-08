class Node:
    """
    Linked List node definition.
    """


    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next_node = None
        self.previous_node = None

class LinkedList:
    """
    Linked list python implementation.
    """


    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def __str__(self):
        _llist = []
        temp_pointer_node = self.head_node
        while temp_pointer_node:
            _llist.append(temp_pointer_node.data)
            temp_pointer_node = temp_pointer_node.next_node
        if len(_llist) > 0:
            return ' '.join(str(i) for i in _llist)
        return '[ ]'
