import typing
from typing import List
from typing import Optional
import math
import functools


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for _ in range(k)]
        self.ptr = 0
        self.curr = 0

    def enQueue(self, value: int) -> bool:
        if self.curr >= len(self.q):
            return False

        self.q[(self.ptr + self.curr) % len(self.q)] = value
        self.curr += 1
        return True

    def deQueue(self) -> bool:
        if not self.curr:
            return False
        self.q[self.ptr] = -1
        self.ptr = (self.ptr + 1) % len(self.q)
        self.curr -= 1
        return True

    def Front(self) -> int:
        if not self.curr:
            return -1
        return self.q[self.ptr]

    def Rear(self) -> int:
        if not self.curr:
            return -1
        return self.q[(self.ptr + self.curr - 1) % len(self.q)]

    def isEmpty(self) -> bool:
        return (self.curr == 0)

    def isFull(self) -> bool:
        return (self.curr == len(self.q))


def main():
    obj = MyCircularQueue(3)

    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.enQueue(5))
    print(obj.Rear())


    exit()

if __name__ == "__main__":
    main()