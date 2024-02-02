import typing
from typing import List
from typing import Optional
import math
import functools

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        i = 0
        j = n - 1

        if n == 1:
            return 0
        while i < n - 1 and height[i] <= height[i + 1]:
            i += 1
        if not i < n:
            return 0

        while j > 0 and height[j] <= height[j - 1]:
            j -= 1

        if j < 0:
            return 0
        if j == i:
            return 0

        curr_sum = 0
        last_i = i
        total_sum = 0

        k = i + 1
        while k < j:

            if height[k] >= height[k + 1] and height[k] > height[k - 1]:
                if height[k] == height[k + 1]:
                    while height[k] == height[k + 1]:
                        k += 1
                    if height[k] > height[k + 1]:
                        if height[last_i] > height[k]:
                            k += 1
                            continue
                        curr_sum = 0
                        for m in range(last_i + 1, k):
                            curr_sum += max(0, min(height[k], height[last_i]) - height[m])
                        total_sum += curr_sum
                        curr_sum = 0
                        last_i = k

                if height[last_i] > height[k]:
                    k += 1
                    continue
                curr_sum = 0
                for m in range(last_i + 1, k):
                    curr_sum += max(0, min(height[k], height[last_i]) - height[m])
                total_sum += curr_sum
                curr_sum = 0
                last_i = k
            k += 1

        if height[last_i] <= height[j]:
            for m in range(last_i + 1, j):
                curr_sum += max(0, height[last_i] - height[m])
            total_sum += curr_sum
            return total_sum

        k = j - 1
        last_t = j
        while k >= last_i + 1:
            if height[k] >= height[k - 1] and height[k] > height[k + 1]:
                if height[k] == height[k - 1]:
                    while height[k] == height[k + 1]:
                        k -= 1
                    if height[k] > height[k - 1]:
                        if height[last_t] > height[k]:
                            k -= 1
                            continue
                        curr_sum = 0
                        m = last_t - 1
                        while m > k:
                            curr_sum += max(0, height[k] - height[m])
                            m -= 1
                        total_sum += curr_sum
                        curr_sum = 0
                        last_t = k

                if height[last_t] > height[k]:
                    k -= 1
                    continue
                curr_sum = 0
                m = last_t - 1
                while m > k:
                    curr_sum += max(0, height[last_t] - height[m])
                    m -= 1
                total_sum += curr_sum
                curr_sum = 0
                last_t = k
            k -= 1

        curr_sum = 0
        for m in range(last_i + 1, last_t):
            curr_sum += max(0, height[last_t] - height[m])
        total_sum += curr_sum

        return total_sum

def main():
    res = Solution.trap(None,[0,1,0,2,1,0,1,3,2,1,2,1])
    print(res)
    exit()

if __name__ == "__main__":
    main()