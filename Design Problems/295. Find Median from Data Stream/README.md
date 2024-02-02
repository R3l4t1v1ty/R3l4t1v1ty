## 295. Find Median from Data Stream

link: https://leetcode.com/problems/find-median-from-data-stream/description/

### Problem:

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

### Constraints:

- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

### Discussing Solution:

We use 2 priority heaps to store input stream. The first one
is for values smaller than our current median value and the
second one is for values that are bigger than our current
median value. 

The median value is equal to the root value of the heap
with more elements (this happens if total number of elements 
inputted is odd) or the average of both root values if 
they have the same amount of members (this happens if total
number of elements inputted is even)

Example:

input: 2

input: 3

input: 4

median?

Now we check what we have in our system.

-3, -2 in low

4 in high

Which gives us 3 as our answer.

> [!Note]
> The values in low array are negated because python only has
> min value priority queue as a built-in data structure.

Now if we input 1, we will have to switch things up a bit in
our queues.

-3 will go from low to high and 1 will go into low.

low: -2, -1

high: 3, 4

And at this point our median is (3+(-(-2)))/2 = 2.5


### Complexities:

- Time: O(log(n)) for each call
- Space: O(n) for storing all input data