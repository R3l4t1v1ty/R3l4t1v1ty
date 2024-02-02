## 2963. Count the Number of Good Partitions

link: https://leetcode.com/problems/count-the-number-of-good-partitions/description/

### Problem:

You are given a 0-indexed array nums consisting of positive integers.

A partition of an array into one or more contiguous subarrays is called good if no two subarrays contain the same number.

Return the total number of good partitions of nums.

Since the answer may be large, return it modulo 10^9 + 7.

### Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

### Discussing Solution:

We count frequencies of elements of an array nums while storing
first and last appearance of each element.

If no element appears twice, every partition of this array is
good partition so we can return the result.

Otherwise, we want to find intervals in which are all members 
fully contained. We sort array where we have first and last
appearances of elements and then merge those intervals that
are overlapping with each other. We can look at resulting
as partition-able parts. So the count of elements that we 
want to make partitions off of is count of intervals plus count
of elements that are not in those intervals.

Finally, we calculate number of partitions with a simple
equation 2^(num of elements-1).


### Complexities:

- Time: O(n*log(n))
- Space: O(n)