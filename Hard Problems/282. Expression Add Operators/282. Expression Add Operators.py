import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        res = []

        def operatorify(cval, lstr, rstr, pval, ppval=None):

            if rstr == "":
                if cval == target:
                    res.append(lstr)
                return

            c = int(rstr[0])
            operatorify(cval + c, lstr + "+" + rstr[0], rstr[1:], c)
            operatorify(cval - c, lstr + "-" + rstr[0], rstr[1:], -c)

            operatorify(cval - pval + pval * c, lstr + "*" + rstr[0], rstr[1:], pval * c, pval)

            if lstr[-1] != "0" or pval:
                if ppval is not None:
                    pom = pval*10+c*ppval
                    operatorify(cval - pval + pom, lstr + rstr[0], rstr[1:], pom, ppval)
                else:
                    pom = pval * 10 + (1 if pval >= 0 else -1)*c
                    operatorify(cval - pval + pom, lstr + rstr[0], rstr[1:], pom)

        operatorify(int(num[0]), num[0], num[1:], int(num[0]), None)
        return res


def main():

    res = Solution.addOperators(None,num = "123", target = 6)
    print(res)
    exit()

if __name__ == "__main__":
    main()