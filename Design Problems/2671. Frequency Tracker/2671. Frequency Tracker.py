import typing
from typing import List
from typing import Optional
import math
import functools


class FrequencyTracker:

    def __init__(self):
        self.hmap = {}
        self.fmap = {}

    def add(self, number: int) -> None:
        if number in self.hmap:
            f = self.hmap[number]

            if self.fmap[f] == 1:
                self.fmap.pop(f)
            else:
                self.fmap[f] -= 1

            self.hmap[number] += 1

            f = self.hmap[number]

            if f in self.fmap:
                self.fmap[f] += 1
            else:
                self.fmap[f] = 1

        else:
            self.hmap[number] = 1
            if 1 in self.fmap:
                self.fmap[1] += 1
            else:
                self.fmap[1] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.hmap:
            f = self.hmap[number]

            if self.fmap[f] == 1:
                self.fmap.pop(f)
            else:
                self.fmap[f] -= 1

            if f == 1:
                self.hmap.pop(number)
            else:
                self.hmap[number] -= 1

                f = self.hmap[number]

                if f in self.fmap:
                    self.fmap[f] += 1
                else:
                    self.fmap[f] = 1

    def hasFrequency(self, frequency: int) -> bool:
        return (frequency in self.fmap)


def main():
    obj = FrequencyTracker()
    print(obj.add(2))
    print(obj.add(2))
    print(obj.hasFrequency(2))
    print(obj.add(1))
    print(obj.deleteOne(2))
    print(obj.hasFrequency(2))
    print(obj.deleteOne(2))
    print(obj.deleteOne(1))
    print(obj.hasFrequency(1))


    exit()

if __name__ == "__main__":
    main()