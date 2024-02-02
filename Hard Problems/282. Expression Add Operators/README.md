## 282. Expression Add Operators

link: https://leetcode.com/problems/expression-add-operators/description/

### Problem:

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

### Constraints:

1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1

### Discussing Solution:

We use backtracking setup to put (+,-,* or nothing) and
try every possible combination to find all of those that give
us our result.

Example:
> "123"
> target = 6

1+2+3

1+2-3

1+2*3

1+23

and then all this repeated 3 additional times with first + being
swapped with -, * and nothing.

While doing that we find out that our target solution of 6
can be achieved with 1+2+3 and 1 * 2 * 3.

### Complexities:

- Time: O(4^n)
- Space: O(n)
- n is the length of num