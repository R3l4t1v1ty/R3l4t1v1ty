import typing
from typing import List
from typing import Optional
import math
import functools

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def create_table(cfg):
            tbl = [["." for _ in range(n)] for _ in range(n)]

            for j,i in enumerate(cfg):
                tbl[i][j] = "Q"

            return ["".join(tbl[i]) for i in range(n)]

        # 1 2 3 4
        # 9*8*7*6*5*4*3*2*1
        arr = []

        def find_queens(table, left):

            if not len(left):
                arr.append(table)
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

        res = []

        for s in arr:
            res.append(create_table(s))

        return res

def main():
    res = Solution.solveNQueens(None,4)
    print(res)
    exit()

if __name__ == "__main__":
    main()