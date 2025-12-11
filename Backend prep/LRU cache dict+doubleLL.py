class _Node:
    __slots__ = ("key","val","prev","next")
    def __init__(self,k,v):
        self.key=k; self.val=v; self.prev=None; self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node
        # sentinel head/tail
        self.head = _Node(None,None)
        self.tail = _Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n; n.prev = p

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        # move to front
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.cap:
                # evict LRU (tail.prev)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            node = _Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

# quick usage:
# c=LRUCache(2); c.put(1,1); c.put(2,2); print(c.get(1)); c.put(3,3); print(c.get(2))
