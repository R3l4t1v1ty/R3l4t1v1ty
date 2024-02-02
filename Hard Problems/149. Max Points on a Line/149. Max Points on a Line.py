import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        maxv = 0
        for i in range(n-1):
            hmap = {}
            for j in range(i+1,n):
                dx = points[i][0]-points[j][0]
                dy = points[i][1]-points[j][1]
                if dx:
                    k = dy/dx
                else:
                    k = 100000
                if k in hmap:
                    hmap[k] += 1
                else:
                    hmap[k] = 1
            for x in hmap:
                if hmap[x] > maxv:
                    maxv = hmap[x]
        return maxv+1

def main():

    res = Solution.maxPoints(None,[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
    print(res)
    exit()

if __name__ == "__main__":
    main()