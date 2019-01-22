class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.key}: {self.val}'

    def remove(self):
    # optional but useful, connects previous link to next link
    # and removes self from list.
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def first(self):
        return self.head.next

    def last(self):
        return self.tail.prev

    def is_empty(self):
        return self.head.next is self.tail

    def __getitem__(self, key):
        for node in self:
            if node.key == key:
                return node.val
        return None

    def __contains__(self, key):
        return True if self[key] else False

    def append(self, key, val):
        node = Node(key, val)
        current_last = self.last
        current_last.next = node
        node.prev = current_last
        self.tail.prev = node
        node.next = self.tail

    def __setitem__(self, key, val):
        for node in self:
            if node.key == key:
                node.val = val

    def remove(self, key):
        for node in self:
            if node.key == key:
                node.remove()
                return node
        return None

    def __iter__(self):
        node = self.first()
        while not node is self.tail:
            yield node
            node = node.next

    def __str__(self):
        res = []
        for node in self:
            res += str(node)
        return ', '.join(res)

