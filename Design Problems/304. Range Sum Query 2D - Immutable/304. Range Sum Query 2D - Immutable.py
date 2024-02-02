import typing
from typing import List
from typing import Optional
import math
import functools


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[i])-1,-1,-1):
                matrix[i][j] += (0 if i == n-1 else matrix[i+1][j]) + (0 if j == m-1 else matrix[i][j+1]) - (0 if (i==n-1 or j==m-1) else matrix[i+1][j+1])
        self.mat = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        n = len(self.mat)
        m = len(self.mat[0])
        res = self.mat[row1][col1]
        if col2 < m-1 and row2 < n-1:
            res += self.mat[row2+1][col2+1]
        if col2 < m-1:
            res -= self.mat[row1][col2+1]
        if row2 < n-1:
            res -= self.mat[row2+1][col1]
        return res


def main():
    obj = NumMatrix([[1,2,3],[4,5,6],[7,8,9]])
    print(obj.sumRegion(0,0,2,2))
    print(obj.sumRegion(1,0,1,2))
    print(obj.sumRegion(2,2,2,2))
    print(obj.sumRegion(0,1,1,2))


    exit()

if __name__ == "__main__":
    main()