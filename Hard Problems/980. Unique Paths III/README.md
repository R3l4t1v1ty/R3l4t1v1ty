## 980. Unique Paths III

link: https://leetcode.com/problems/unique-paths-iii/description/

### Problem:

You are given an m x n integer array grid where grid[i][j] could be:

- 1 representing the starting square. There is exactly one starting square.
- 2 representing the ending square. There is exactly one ending square.
- 0 representing empty squares we can walk over.
- -1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

### Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- 1 <= m * n <= 20
- -1 <= grid[i][j] <= 2
- There is exactly one starting cell and one ending cell.

### Discussing Solution:

First we find the starting cell and we count all the empty
cells.

Then we recursively walk from the starting cell to every other
not already visited cell. When we reach the end cell, we check
if cells passed length is equal to the empty cell count. If it is,
we found one unique path, if it is not, we treat it like a dead end.


### Complexities:

- Time: O(4^(m*n))
- Space: O(m*n)