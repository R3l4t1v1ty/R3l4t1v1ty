import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)

        stolice = 0
        mesta = []
        a = 0
        res = 1
        for i in range(n):
            if corridor[i] == "S":
                stolice += 1
                if stolice == 3:
                    stolice -= 2
                    if a:
                        res *= a
                        a = 0
            if stolice == 2:
                a += 1
        if stolice != 2:
            return 0

        return res % (10 ** 9 + 7)


def main():

    res = Solution.numberOfWays(None,corridor = "SSPPSPS")
    print(res)
    exit()

if __name__ == "__main__":
    main()