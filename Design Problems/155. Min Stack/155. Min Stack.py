import typing
from typing import List
from typing import Optional
import math
import functools


class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = [2 ** 32]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.stack.pop(-1)
        self.mins.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())


    exit()

if __name__ == "__main__":
    main()