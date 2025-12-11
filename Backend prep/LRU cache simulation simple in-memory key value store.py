from collections import OrderedDict

class KeyValueStore:
    """
    A simple in-memory Key-Value store with Least Recently Used (LRU) eviction policy.
    Uses OrderedDict to maintain the order of usage.
    """
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        # OrderedDict maintains insertion order, which we use to track LRU
        self.store = OrderedDict()

    def get(self, key):
        """
        Retrieves the value for a key and updates its usage (moves to the end).
        O(1) average time complexity.
        """
        if key not in self.store:
            return None
        
        # 1. Update usage: Move the key to the end (most recently used)
        value = self.store.pop(key)
        self.store[key] = value
        return value

    def set(self, key, value):
        """
        Adds or updates a key-value pair. Evicts LRU if capacity is reached.
        O(1) average time complexity.
        """
        if key in self.store:
            # Update: Move to the end and update value
            self.store.pop(key)
        
        elif len(self.store) >= self.capacity:
            # Eviction: Pop the first item (Least Recently Used)
            self.store.popitem(last=False)
            
        # Insert/Update the new key-value pair (at the end, making it MRU)
        self.store[key] = value
        
    def __repr__(self):
        return f"KeyValueStore(capacity={self.capacity}, items={list(self.store.keys())})"
