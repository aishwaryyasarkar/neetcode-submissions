class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}    
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left

    # insert in LL and update hashmap    
    def insert(self, node):
        # incoming pointers
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev, nxt
    
    def remove(self, node):
        node.prev.nxt, node.nxt.prev = node.nxt, node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # TODO: move used key to right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # why are we removing the whole thing, and not just updating its value?
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.nxt # the head node
            self.remove(lru)
            del self.cache[lru.key]



        
