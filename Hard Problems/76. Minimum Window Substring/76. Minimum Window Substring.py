import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        def check_maps():

            for key in hmap:
                if not (key in cmap and hmap[key] <= cmap[key]):
                    return False
            return True

        if m == 0 or m < n:
            return ""
        if n == 0:
            return s

        hmap = {}
        cmap = {}
        mini = 0
        minj = m + 1

        for ch in t:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1

        i = 0
        j = 0

        while j < n:
            if s[j] in cmap:
                cmap[s[j]] += 1
            else:
                cmap[s[j]] = 1
            j += 1

        while j < m:
            check = check_maps()
            if not check:
                if s[j] in cmap:
                    cmap[s[j]] += 1
                else:
                    cmap[s[j]] = 1
                j += 1
            else:
                if j - i < minj - mini:
                    minj = j
                    mini = i

                if cmap[s[i]] > 1:
                    cmap[s[i]] -= 1
                else:
                    cmap.pop(s[i])
                i += 1

        while i < m:
            check = check_maps()

            if check:
                if j - i < minj - mini:
                    minj = j
                    mini = i

                if cmap[s[i]] > 1:
                    cmap[s[i]] -= 1
                else:
                    cmap.pop(s[i])
                i += 1
            else:
                break
        if minj == m + 1:
            return ""
        return s[mini:minj]

def main():
    res = Solution.minWindow(None,s = "ADOBECODEBANC", t = "ABC")
    print(res)
    exit()

if __name__ == "__main__":
    main()