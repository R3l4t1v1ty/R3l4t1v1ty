import typing
from typing import List
from typing import Optional
import math
import functools
import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) and len(self.right):
            if len(self.left) == len(self.right):
                if -self.left[0] >= num:
                    heapq.heappush(self.left,-num)
                else:
                    heapq.heappush(self.right,num)
                    heapq.heappush(self.left,-heapq.heappop(self.right))
            else:
                if -self.left[0] >= num:
                    heapq.heappush(self.left,-num)
                    heapq.heappush(self.right,-heapq.heappop(self.left))
                else:
                    heapq.heappush(self.right,num)
        elif len(self.left):
            if -self.left[0] > num:
                self.right.append(-self.left[0])
                self.left[0] = -num
            else:
                self.right.append(num)
        else:
            self.left.append(-num)

    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return (self.right[0] - self.left[0]) / 2
        return -self.left[0]

def main():
    mdf = MedianFinder()
    mdf.addNum(2)
    mdf.addNum(3)
    mdf.addNum(4)
    print(mdf.findMedian())
    mdf.addNum(1)
    print(mdf.findMedian())
    mdf.addNum(5)
    mdf.addNum(6)
    print(mdf.findMedian())
    exit()

if __name__ == "__main__":
    main()