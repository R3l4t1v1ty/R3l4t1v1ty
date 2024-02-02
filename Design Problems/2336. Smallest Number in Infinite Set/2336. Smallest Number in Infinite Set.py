import typing
from typing import List
from typing import Optional
import math
import functools
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i for i in range(1,1001)]
        heapq.heapify(self.arr)
        self.set = set(self.arr)

    def popSmallest(self) -> int:
        a = heapq.heappop(self.arr)
        self.set.remove(a)
        return a

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.arr,num)
            self.set.add(num)


def main():
    obj = SmallestInfiniteSet()
    print(obj.addBack(2))
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.addBack(1))
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())


    exit()

if __name__ == "__main__":
    main()