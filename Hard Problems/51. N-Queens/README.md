## 42. N-Queens

link: https://leetcode.com/problems/n-queens/description/

### Problem:

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

### Constraints:

- 1 <= n <= 9

### Discussing Solution:

If we want to put n queens on n x n board, the obvious
constraint is that not 2 queens share the same row or column.

We can use that observation to our advantage if we write
down an array of the size n where the index is the number of row
and value is the number of column one queen is placed.

We create that array recursively by placing the next queen on
the next possible column in her row (we have to check if 
previous queens hit the new queen diagonally). 

If we manage to finish that array, that means that we found
one of the solutions.

When we find all solution, we just need to parse them into 
valid board states and return them as a result.

### Complexities:

- Time: O(n^n)
- Space: O(n)