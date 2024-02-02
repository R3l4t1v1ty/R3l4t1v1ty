import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:

        def myfun(e):
            return e[0]

        def mod_pow(b, e, m):
            if m == 1:
                return 0
            c = 1
            for i in range(e):
                c = (c * b) % m
            return c

        hmap = {}
        li = []

        for i, num in enumerate(nums):
            if num in hmap:
                hmap[num].append(i)
                if len(hmap[num]) == 2:
                    li.append(hmap[num])
            else:
                hmap[num] = [i]

        if len(li) == 0:
            return mod_pow(2, len(nums) - 1, 10 ** 9 + 7)

        li.sort(key=myfun)

        nli = []

        i = 0
        k = 0

        while i < len(li):
            nli.append(li[i])
            if len(nli) == 1:
                k += nli[-1][0]
            else:
                k += nli[-1][0] - nli[-2][-1] - 1
            j = i + 1

            while j < len(li) and nli[-1][-1] > li[j][0]:
                nli[-1][-1] = max(nli[-1][-1], li[j][-1])
                j += 1

            i = j

        k += len(nums) - nli[-1][-1] - 1

        k += len(nli)

        return mod_pow(2, k - 1, 10 ** 9 + 7)


def main():

    res = Solution.numberOfGoodPartitions(None,nums = [1,2,1,3])
    print(res)
    exit()

if __name__ == "__main__":
    main()