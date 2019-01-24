# TODO: Test
from linked_list import LinkedList, Node
from hash_map import HashMap

class LRUCache:
    def __init__(self, cache_size):
        self.map = HashMap()
        self.store = LinkedList()
        self.cache_size = cache_size

    def count(self):
        return len(self.map)

    def __getitem__(self, key):
        if self.map[key]:
            node = self.map[key]
            self.update_node(node) # Because this is now the most recently seen object. i.e. keep it in cache
            return node.val
        return False

    def __str__(self):
        return 'Map: ' + str(self.map) + '\n' + 'Store: ' + str(self.store)

    def __setitem__(self, key, val):
        if key in self.map:
            self.map[key].val = val
            self.update_node(self.map[key])
        else:
            new_node = self.store.append(key, val)
            self.map[key] = new_node
        if self.count() > self.cache_size:
            self.eject()
        return val            
  
    def update_node(self, node):
        node.remove()
        self.store.append(node.key, node.val)

    def eject(self):
        rm_node = self.store.first()
        rm_node.remove()
        self.map.delete(rm_node.key)

