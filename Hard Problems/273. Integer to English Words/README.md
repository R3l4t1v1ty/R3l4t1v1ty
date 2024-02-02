## 273. Integer to English Words

link: https://leetcode.com/problems/integer-to-english-words/description/

### Problem:

Convert a non-negative integer num to its English words representation.

### Constraints:

- 0 <= num <= 23^1 - 1

### Discussing Solution:

First we need to map certain numbers to their english words. (1-20,
decades, 100, 1000, 1000000)

Then we create a function that returns english interpretation of
an up to 3 digit long number.

Then we split our input numbers in parts of length of 3 and
give them to the function that gives us words. We put a 
prefix of nothing, thousand, million, ...

And we have our solution.

### Complexities:

- Time: O(n)
- Space: O(1)
- n is number of digits of num