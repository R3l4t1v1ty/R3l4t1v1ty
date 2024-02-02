import typing
from typing import List
from typing import Optional
import math
import functools

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def check_row(e):
            for i in range(n):
                if board[e[0]][i] == str(e[2]):
                    return False
            return True

        def check_column(e):
            for i in range(n):
                if board[i][e[1]] == str(e[2]):
                    return False
            return True

        def check_square(e):
            a = (e[0] // 3) * 3
            b = (e[1] // 3) * 3

            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    if board[i][j] == str(e[2]):
                        return False
            return True

        def check(e):
            return (check_row(e) and check_column(e) and check_square(e))

        entries = []
        n = 9
        i = 0
        j = 0
        lv = 0
        while i < n:
            j = 0
            while j < n:
                if board[i][j] == ".":
                    v = 1
                    if lv:
                        v = lv + 1
                        lv = 0
                    b = True
                    while v <= 9:
                        entry = [i, j, v]
                        if check(entry):
                            b = False
                            board[i][j] = str(v)
                            entries.append(entry)
                            break
                        v += 1
                    if b:
                        entry = entries.pop(-1)
                        i = entry[0]
                        j = entry[1]
                        board[i][j] = "."
                        lv = entry[2]
                        continue

                j += 1
            i += 1

def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution.solveSudoku(None,board)

    for row in board:
        print(row)
    exit()

if __name__ == "__main__":
    main()