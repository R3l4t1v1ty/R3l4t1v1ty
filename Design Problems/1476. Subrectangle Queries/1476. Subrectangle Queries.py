import typing
from typing import List
from typing import Optional
import math
import functools


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.rect[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]


def main():
    obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
    print(obj.getValue(0,2))
    print(obj.updateSubrectangle(0,0,3,2,5))
    print(obj.getValue(0,2))
    print(obj.getValue(3,1))
    print(obj.updateSubrectangle(3,0,3,2,10))
    print(obj.getValue(3,1))
    print(obj.getValue(0,2))


    exit()

if __name__ == "__main__":
    main()