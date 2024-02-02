import typing
from typing import List
from typing import Optional
import math
import functools


class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        n = len(password)

        result = 0

        lowercase = 0
        uppercase = 0
        digit = 0

        for ch in password:
            if ch.isdigit():
                digit += 1
            elif ch.islower():
                lowercase += 1
            elif ch.isupper():
                uppercase += 1

        result += (not lowercase) + (not uppercase) + (not digit)

        if n <= 20:

            tochange = 0

            curr = password[0]
            count = 1
            for i in range(1, n):
                if curr == password[i]:
                    count += 1
                else:
                    curr = password[i]
                    if count > 2:
                        tochange += count // 3
                    count = 1
            if count > 2:
                tochange += count // 3

            if n < 6:
                result = max(6 - n, result)

            elif n >= 6 and n <= 20:
                result = max(result, tochange)

        else:

            maxtoremove = 0
            cluster = []

            curr = password[0]
            count = 1
            for i in range(1, n):
                if curr == password[i]:
                    count += 1
                else:
                    curr = password[i]
                    if count > 2:
                        maxtoremove += count - 2
                        cluster.append(count)
                    count = 1
            if count > 2:
                maxtoremove += count - 2
                cluster.append(count)

            if maxtoremove > n - 20:

                k = n - 20  # maxtoremove-n+20
                a = 0
                while k > a:
                    i = 0
                    while k > a and i < len(cluster):
                        if cluster[i] % 3 == 0:
                            cluster[i] -= 1
                            a += 1
                        i += 1
                    i = 0
                    while k > a and i < len(cluster):
                        if cluster[i] % 3 == 1:
                            cluster[i] -= 1
                            a += 1
                            if k == a:
                                break
                            cluster[i] -= 1
                            a += 1
                        i += 1
                    i = 0
                    while k > a and i < len(cluster):
                        if cluster[i] != 2 and cluster[i] % 3 == 2:
                            cluster[i] -= 1
                            a += 1
                            if k == a:
                                break
                            cluster[i] -= 1
                            a += 1
                            if k == a:
                                break
                            cluster[i] -= 1
                            a += 1
                        i += 1

                tochange = 0
                for i in range(len(cluster)):
                    if cluster[i] > 2:
                        tochange += cluster[i] // 3

                result = n - 20 + max(result, tochange)

                # treba da se od clustera najoptimalnije oduzme k karaktera sto znaci
                # da treba da se skidaju prvo 3, 6, 9 nodovi po jedan, pa kad ih nema vise
                # nebitno
                # aaaaabaaaaabaaaaaaaabaaaaa
                # 12345678901234567890123456789 -> 29
                # clusters -> [5,6,9,6] -> [5,5,8,5] -> [5,5,8,5] (1,1,2,1)

            else:

                result += n - 20

        return result


def main():

    res = Solution.strongPasswordChecker(None,password = "1337C0d3")
    print(res)
    exit()

if __name__ == "__main__":
    main()