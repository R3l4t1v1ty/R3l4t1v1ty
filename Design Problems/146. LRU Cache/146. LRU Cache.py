import typing
from typing import List
from typing import Optional
import math
import functools


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.memory = {}

    def get(self, key: int) -> int:
        res = self.memory.get(key,-1)
        if res == -1:
            return -1
        self.memory.pop(key)
        self.memory[key] = res
        return res

    def put(self, key: int, value: int) -> None:
        if self.memory.get(key):
            self.memory.pop(key)
            self.memory[key] = value
        else:
            if len(self.memory) == self.cap:
                self.memory.pop(next(iter(self.memory)))
            self.memory[key] = value


def main():
    obj = LRUCache(3)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1))
    obj.put(3,3)
    obj.put(4,4)
    print(obj.get(1))
    print(obj.get(2))
    print(obj.get(4))


    exit()

if __name__ == "__main__":
    main()