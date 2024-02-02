## 41. First Missing Positive

link: https://leetcode.com/problems/first-missing-positive/description/

### Problem:

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

### Constraints:

- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

### Discussing Solution:

Because we are trying to find the smallest missing positive 
integer, and arrays are indexed with the smallest positive 
integers shifted by one to the right, we can use that to our
advantage.

We traverse our array and when we find a positive number 
we flag an index at that number minus one. Then we traverse the array 
again in a search for the first non flagged index. That index
increased by 1 is our solution.

Example:

>nums: [3,-1,-2,0,-3,1]

3 is positive integer, so we flag index 2 and take a number
from that index and repeat this check for it as well. -2 is
not a positive integer, so we just replace 3 with it and continue

>nums: [-2,-1,None,0,-3,1]

-1 is not a positive integer

None is flagged spot, we skip it since we already check for it's
past inhabitant.

0 is not a positive integer

-3 is not a positive integer

1 is a positive integer! We flag index 0 and check its
inhabitant -2 if it's positive. It's not so we can proceed.

>nums: [None,-1,None,0,-3,-2]

We reached the end, so now we find first index that's not flagged
which is 1. That means out result is 1+1=2.

### Complexities:

- Time: O(n)
- Space: O(1)