import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        digit_names = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            0: ""
        }
        decade_names = {
            1: ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"],
            2: ["Twenty"],
            3: ["Thirty"],
            4: ["Forty"],
            5: ["Fifty"],
            6: ["Sixty"],
            7: ["Seventy"],
            8: ["Eighty"],
            9: ["Ninety"],
            0: [""]
        }
        hundred = "Hundred"
        pow3_names = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion"
        }

        def getsub1000name(n):
            a = n // 100
            b = (n - a * 100) // 10
            c = n % 10
            res = []
            if a:
                res.append(digit_names[a])
                res.append(hundred)

            if b == 1:
                res.append(decade_names[b][c])
            else:
                if b:
                    res.append(decade_names[b][0])
                if c:
                    res.append(digit_names[c])

            return " ".join(res)

        result = []
        c = 0
        while num:
            k = num % 1000
            txt = getsub1000name(k)
            if txt == "":
                c += 1
                num //= 1000
                continue
            if c:
                txt += " " + pow3_names[c]
            result.append(txt)
            c += 1
            num //= 1000
        result.reverse()
        # return result
        return " ".join(result)


def main():

    res = Solution.numberToWords(None,1234567)
    print(res)
    exit()

if __name__ == "__main__":
    main()