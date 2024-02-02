import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn = len(s)
        pn = len(p)

        @functools.cache
        def match(si, pi):

            if pi == pn:
                return (si == sn)
            elif si > sn:
                return False

            if si >= sn:
                for i in range(pi,pn):
                    if p[i] != "*":
                        return False
                return True

            if p[pi] == "*":
                return (match(si+1, pi) or match(si+1,pi+1) or match(si,pi+1))

            if p[pi] == "?" or p[pi] == s[si]:
                return match(si + 1, pi + 1)

            return False

        return match(0, 0)

def main():
    res = Solution.isMatch(None,"abwbcabczzzde","a*bc???de")
    print(res)
    exit()

if __name__ == "__main__":
    main()