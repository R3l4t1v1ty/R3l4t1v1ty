import typing
from typing import List
from typing import Optional
import math
import functools

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        m = len(words)
        l = len(words[0])
        N = m * l
        i = 0
        res = []

        hmap = {}
        pmap = {}

        for word in words:
            if word in hmap:
                hmap[word] += 1
            else:
                hmap[word] = 1

        for i in range(l):
            pmap = {}
            k = 0
            for j in range(i, n - l + 1, l):
                p = s[j:j + l]
                if p in hmap:
                    if p in pmap:
                        pmap[p] += 1
                    else:
                        pmap[p] = 1
                    k += 1
                else:
                    k = 0
                    pmap = {}

                if k == m:

                    b = True

                    for key in hmap:
                        if not pmap.get(key):
                            b = False
                            break
                        if pmap[key] != hmap[key]:
                            b = False
                            break

                    if b:
                        res.append(j - (m - 1) * l)
                    t = s[j - (m - 1) * l:j - (m - 2) * l]
                    if pmap[t] == 1:
                        pmap.pop(t)
                    else:
                        pmap[t] -= 1
                    k -= 1

        return res

def main():

    arr = Solution.findSubstring(None,"abarfoofoobarthefoobarman",["bar","foo","the"])

    print(arr)
    exit()

if __name__ == "__main__":
    main()