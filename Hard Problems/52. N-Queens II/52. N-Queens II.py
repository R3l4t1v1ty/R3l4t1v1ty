import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def totalNQueens(self, n: int) -> int:

        res = [0]

        def find_queens(table, left):

            if not len(left):
                res[0] += 1
                return

            opts = {x for x in left}

            for j, y in enumerate(table):
                opts.discard(y - len(table) + j)
                opts.discard(y + len(table) - j)

            for x in opts:
                a = set(left)
                a.remove(x)
                find_queens(table + [x], a)

        find_queens([], {i for i in range(n)})

        return res[0]

def main():
    res = Solution.totalNQueens(None,4)
    print(res)
    exit()

if __name__ == "__main__":
    main()