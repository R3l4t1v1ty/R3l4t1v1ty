## 23. Merge k Sorted Lists

link: https://leetcode.com/problems/merge-k-sorted-lists/description/

### Problem:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Constraints:

- k == lists.length
- 0 <= k <= 104
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

### Discussing Solution:

The basic idea is to just merge list with a result one by one.
It's fine idea, but we can try to improve it by using divide and conquer idea.
Concretly the idea of merge sort is perfect for this problem. 
Instead of making one big result that we have to traverse every time
we can divide the problem in 2 subproblems, and then those 2 into 4...

Example:

>((1,2,3),(2,4,6),(3,6,12),(4,8,16))

after the first step we will have

>(1,2,2,3,4,6) and (3,4,6,8,12,16)

and then after second step we will get our solution

>(1,2,2,3,3,4,4,6,6,8,12,16)


### Complexities:

- Time: O(N*log(k))
- Space: O(log(k))
- N - total number of nodes
- k - number of lists at the begining