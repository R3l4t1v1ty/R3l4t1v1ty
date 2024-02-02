import typing
from typing import List
from typing import Optional
import math
import functools

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.append(nums[0])
        n = len(nums)

        for i in range(n):

            if nums[i] is not None:
                x = nums[i]

                while x is not None and x > 0 and x < n:
                    pom = nums[x - 1]
                    nums[x - 1] = None
                    x = pom

        for i in range(n):
            if nums[i] is not None:
                return i + 1

        return -1

def main():
    res = Solution.firstMissingPositive(None,[3,-1,-2,0,-3,1,2])
    print(res)
    exit()

if __name__ == "__main__":
    main()