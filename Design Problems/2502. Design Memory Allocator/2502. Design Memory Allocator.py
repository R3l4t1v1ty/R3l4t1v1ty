import typing
from typing import List
from typing import Optional
import math
import functools


class Allocator:

    def __init__(self, n: int):
        self.blocks = [[0, n]]  # chunks of free memory, semiopen intervals
        self.used = {}  # mID:[[start,end],...]

    def allocate(self, size: int, mID: int) -> int:
        for i, b in enumerate(self.blocks):
            if b[1] - b[0] >= size:
                new_chunk = [b[0], b[0] + size]
                if b[0] + size == b[1]:
                    self.blocks.pop(i)
                else:
                    b[0] = b[0] + size
                if mID in self.used:
                    self.used[mID].append(new_chunk)
                else:
                    self.used[mID] = [new_chunk]
                return new_chunk[0]
        return -1

    def free(self, mID: int) -> int:

        if mID not in self.used:
            return 0
        f = 0
        for c in self.used[mID]:
            f += self.deallocate(c)
        self.used.pop(mID)
        return f

    def deallocate(self, chunk):
        n = len(self.blocks)
        i = 0
        csize = chunk[1] - chunk[0]
        if not n:
            self.blocks.append(chunk)
            return csize
        while i < n and chunk[0] > self.blocks[i][0]:
            i += 1

        if i == n:
            if chunk[0] == self.blocks[n - 1][1]:
                self.blocks[n - 1][1] = chunk[1]
            else:
                self.blocks.append(chunk)
            return csize

        if i == 0:
            if chunk[1] == self.blocks[0][0]:
                self.blocks[0][0] = chunk[0]
            else:
                self.blocks.insert(0, chunk)
            return csize

        if chunk[0] != self.blocks[i - 1][1] and chunk[1] != self.blocks[i][0]:
            self.blocks.insert(i, chunk)
        elif chunk[0] != self.blocks[i - 1][1] and chunk[1] == self.blocks[i][0]:
            self.blocks[i][0] = chunk[0]
        elif chunk[0] == self.blocks[i - 1][1] and chunk[1] != self.blocks[i][0]:
            self.blocks[i - 1][1] = chunk[1]
        else:
            self.blocks[i - 1][1] = self.blocks[i][1]
            self.blocks.pop(i)
        return csize


def main():
    obj = Allocator(10)
    print(obj.allocate(1,1))
    print(obj.allocate(1,2))
    print(obj.allocate(1,3))
    print(obj.free(2))
    print(obj.allocate(3,4))
    print(obj.allocate(1,1))
    print(obj.allocate(1,1))
    print(obj.free(1))
    print(obj.allocate(10,2))
    print(obj.free(7))


    exit()

if __name__ == "__main__":
    main()