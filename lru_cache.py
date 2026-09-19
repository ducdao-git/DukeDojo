from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # key in cache, update the value
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        # cache is full, remove least used key
        if self.capacity == len(self.cache):
            self.cache.popitem(last=False)

        # key not in cache, cache not full, add key to cache
        self.cache[key] = value
        self.cache.move_to_end(key)
        return
