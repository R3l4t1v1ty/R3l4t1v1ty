import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        n = bin(n)[2:]
        a = 1 << (len(n))
        s = 1
        rez = 0
        for i in range(len(n)):
            if n[i] == "1":
                rez += s * (a - 1)
                s *= -1
            a >>= 1
        return rez


def main():

    res = Solution.minimumOneBitOperations(None,n = 18)
    print(res)
    exit()

if __name__ == "__main__":
    main()