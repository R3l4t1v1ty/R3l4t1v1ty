import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def calculate(self, s: str) -> int:

        def calc_without_parenthesis(s, i):
            operator = None
            res = None
            while i < len(s):

                if s[i] == " ":
                    i += 1
                    continue

                elif s[i] == "(":
                    pomres, end = calc_without_parenthesis(s, i + 1)
                    i = end + 1

                    if res is None:
                        if operator is None:
                            res = pomres
                        else:
                            res = -pomres
                    else:
                        if operator == "+":
                            res += pomres
                        else:
                            res -= pomres
                    continue

                elif s[i] == ")":
                    return (res, i)

                elif s[i] == "+":
                    operator = "+"
                    i += 1
                    continue
                elif s[i] == "-":
                    operator = "-"
                    i += 1
                    continue
                a = 0
                while i<len(s) and s[i].isdigit():
                    a *= 10
                    a += int(s[i])
                    i+=1

                if res is None:
                    if operator is None:
                        res = a
                    else:
                        res = -a
                else:
                    if operator == "+":
                        res += a
                    else:
                        res -= a
            return res

        res = calc_without_parenthesis(s, 0)

        return res

def main():

    res = Solution.calculate(None,s = "(1+(4+5+2)-3)+(6+8)")
    print(res)
    exit()

if __name__ == "__main__":
    main()