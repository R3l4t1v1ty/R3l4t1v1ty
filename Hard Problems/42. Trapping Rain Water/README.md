## 42. Trapping Rain Water

link: https://leetcode.com/problems/trapping-rain-water/description/

### Problem:

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it 
can trap after raining.

### Constraints:

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

### Discussing Solution:

First, we can trim our input from the both sides. Until we find
the first index where ***height[i] < height[i-1]*** from 
the left or ***height[i] > height[i-1]*** from the right.

Now we take what's left and search for local maximums.
When we find 2 local maximums we can fill the area between them
with water to the level of the smaller one but that runs into 
a problem where one local maximum is surrounded with 2 bigger 
local maximums. So we have to account for that as well.
We can do that by searching two local maximums where the 
second one is bigger than the first one. That works. But now
we have to take care of the situation where we never find the
bigger local maximum. We do that by going from the other side
of the array until we reach that local maximum from earlier.

Example:

>height: [0,1,3,2,1,2,1,2,3,2,3,1]

First we trim our heights.

>height: [3,2,1,2,1,2,3,2,3]

Now we start our search for local maximums

First one is 3, second one is 2, third one is 3.

We can fill that "tub" between 3 and 3 with 7 water tiles.

Now we have 3 as a first local maximum, and we find the second
one at the height 3 as well.

We can fill that "tub" with 1 water tile.

That local maximum was at the end of our trimmed array so our 
solution is 8.


### Complexities:

- Time: O(n)
- Space: O(1)