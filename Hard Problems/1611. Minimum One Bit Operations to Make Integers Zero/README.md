## 1611. Minimum One Bit Operations to Make Integers Zero

link: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/

### Problem:

Given an integer n, you must transform it into 0 using the following operations any number of times:

- Change the rightmost (0th) bit in the binary representation of n.
- Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.

Return the minimum number of operations to transform n into 0.

### Constraints:

- 0 <= n <= 10^9

### Discussing Solution:

There is a math trick in this problem. 
> 2^k needs 2^(k+1)-1 operations to become 0

> to get from a to b we need the same amount of steps as we need
> to get from b to a.

This we just have to add or subtract 2^(k+1)-1 for each bit that's 1.

Example:

> 10010

We have can split that in 2 numbers

> 10000 and 00010

To get from 10000 to 00000 we need 2^(5)-1

But we are already 2^(2)-1 steps away from 0:

To get from 00010 to 00000 we need 2^(2)-1

That means that we need 2^(5)-2^(2) steps to get to 0.


### Complexities:

- Time: O(log(n))
- Space: O(1)