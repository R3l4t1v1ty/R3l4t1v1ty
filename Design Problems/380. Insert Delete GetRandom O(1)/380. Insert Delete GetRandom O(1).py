import typing
from typing import List
from typing import Optional
import math
import functools
import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            i = self.map[val]
            self.arr[i] = self.arr[-1]
            self.map[self.arr[-1]] = i
            self.arr.pop(-1)
            self.map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


def main():
    obj = RandomizedSet()

    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.insert(3))
    print(obj.getRandom())
    print(obj.remove(2))
    print(obj.getRandom())



    exit()

if __name__ == "__main__":
    main()