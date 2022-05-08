# https://leetcode.com/problems/lru-cache/
# 05/07/2022

import llist

class LRUCache:
    """
    Least Recenet Used Cache implementation
    """


    def __init__(self, capacity):
        if capacity <= 0:
            print("Capacity needs to be greater than 0.")
            return
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def __str__(self):
        _llist = []
        temp_pointer_node = self.head
        while temp_pointer_node:
            _llist.append((temp_pointer_node.key, temp_pointer_node.data))
            temp_pointer_node = temp_pointer_node.next_node
        if len(_llist) > 0:
            return ' '.join(str(i) for i in _llist)
        return '[ ]'

    def prepend_node(self, node):
        """
        Prepend node to existing cache
        """

        if not self.head:
            self.head = self.tail = node
        else:
            self.head.previous_node = node
            node.next_node = self.head
            self.head = node

    def unlink_node(self, node):
        """
        Remove node from cache
        """
        if self.tail is node:
            self.tail = node.previous_node
            if node.previous_node:
                node.previous_node.next_node = None
            return

        node.next_node.previous_node = node.previous_node
        node.previous_node.next_node = node.next_node

    def get(self, key):
        """
        Retrieve value by key from the cache
        """
        if key not in self.map:
            return -1

        node = self.map[key]

        if node is not self.head:
            self.unlink_node(node)
            self.prepend_node(node)

        return node.data

    def put(self, key, value):
        """
        add value in the cache
        """
        if key in self.map:
            node = self.map[key]
            node.data = value
            self.get(key)
            return

        if len(self.map) >= self.capacity:

            if self.capacity == 1:
                self.map = {}
                self.head = None
                self.tail = None

            else:
                _key = self.tail.key
                self.map.pop(_key)
                self.unlink_node(self.tail)

        new_node = llist.Node(value, key)
        self.map[key] = new_node
        self.prepend_node(new_node)
