import typing
from typing import List
from typing import Optional
import math
import functools


class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [-1 for _ in range(k)]
        self.start = 0
        self.end = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.start = (self.start - 1) % self.capacity
        self.dq[self.start] = value

        if self.isEmpty():
            self.end = self.start

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.end = (self.end + 1) % self.capacity
        self.dq[self.end] = value

        if self.isEmpty():
            self.start = self.end

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1
        self.end = (self.end - 1) % self.capacity
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.dq[self.start]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.dq[self.end]

    def isEmpty(self) -> bool:
        return (self.size == 0)

    def isFull(self) -> bool:
        return (self.size == self.capacity)


def main():
    obj = MyCircularDeque(3)
    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.getRear())
    print(obj.isFull())
    print(obj.deleteLast())
    print(obj.insertFront(4))
    print(obj.getFront())


    exit()

if __name__ == "__main__":
    main()