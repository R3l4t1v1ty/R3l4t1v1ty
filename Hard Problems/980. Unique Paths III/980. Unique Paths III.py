import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = [0]
        t = 0
        n = len(grid)
        m = len(grid[0])
        si, sj = 0,0
        for i in range(n):
            for j in range(m):
                t += (grid[i][j] == 0)
                if grid[i][j] == 1:
                    si,sj = i,j
        w = [(0,1),(1,0),(0,-1),(-1,0)]

        def walk(i,j,visited):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == -1 or (i,j) in visited:
                return

            if len(visited) == t+1 and grid[i][j] == 2:
                res[0] += 1
                return
            visited.add((i,j))
            for v in w:
                walk(i+v[0],j+v[1],visited)
            visited.remove((i,j))

        walk(si,sj,set())
        return res[0]


def main():

    res = Solution.uniquePathsIII(None,grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(res)
    exit()

if __name__ == "__main__":
    main()