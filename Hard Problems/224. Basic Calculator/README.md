## 224. Basic Calculator

link: https://leetcode.com/problems/basic-calculator/description/

### Problem:

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

### Constraints:

- 1 <= s.length <= 3 * 105
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

### Discussing Solution:

We recursively solve our problem by solving each pair of parenthesis first, 
from the more nested ones to the least nested ones.

A part without parenthesis is trivial to solve just by correctly
parsing that part of the string.

Example:

>"(1+(4+5+2)-3)+(6+8)"

We solve (4+5+2) first to be 11

Then we solve (1+11-3) to be 9

Then we solve (6+8) to be 14

And finally we solve 9+14 to be 23.

### Complexities:

- Time: O(n)
- Space: O(n)