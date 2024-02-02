## 37. Sudoku Solver

link: https://leetcode.com/problems/sudoku-solver/description/

### Problem:

Write a program to solve a Sudoku puzzle by filling the empty 
cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 
9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

### Constraints:

- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'

### Discussing Solution:

Bruteforce. We find first empty tile, find the first number that
can be placed there and continue. When we can't find a number
for a tile, we have to go back and change the last entry to some
other number.

Example:

board:

>53..7....

>6..195...

>.98....6.

>8...6...3

>4..8.3..1

>7...2...6

>.6....28.

>...419..5

>....8..79

Tile (0,2) is the first empty tile. We can fill it with 1.

Tile (0,3) is the next empty tile. We can't fill it with 1,
but we can with 2

Tile (0,5) is the next empty tile. We can fill it with 4.

Tile (0,6) is the next empty tile. We can fill it with 8.

Tile (0,7) is the next empty tile. We can fill it with 9.

Tile (0,8) is the next empty tile. We can't fill it with 
any number. So we go back.

Now that means that tile (0,7) can't be 9, and that means
that tile (0,7) can't be filled with any number, so we have
to go even further back.

Tile (0,6) can't stay 8 so now we try to put 9 there.

And we repeat this process until we fill every tile on the 
board with numbers.


### Complexities:

- Time: O(1)
- Space: O(1)
- if sudoku board size wasn't fixed 9, the complexities would 
be O(n!^n) and O(n^2) respectively.