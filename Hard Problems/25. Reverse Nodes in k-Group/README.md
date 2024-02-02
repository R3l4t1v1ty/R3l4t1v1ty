## 25. Reverse Nodes in k-Group

link: https://leetcode.com/problems/reverse-nodes-in-k-group/

### Problem:

Given the head of a linked list, reverse the nodes of the list 
***k*** at a time, and return the modified list.

***k*** is a positive integer and is less than or equal to the 
length of the linked list. If the number of nodes is not a 
multiple of ***k*** then left-out nodes, in the end, should 
remain as it is.

You may not alter the values in the list's nodes, only nodes 
themselves may be changed.

### Constraints:

- The number of nodes in the list is ***n***.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

### Discussing Solution:

We can go through the list, count nodes and when we get to
k we that those nodes and call function to reverse them. Then 
we return them to our list and continue counting again from 0.

Example:

list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8

k: 3

First step:

>1->2->3 | 4->5->6->7->8

>1->2->3 becomes 3->2->1

And we put it back into the list

>3->2->1 -> 4->5->6->7->8

Second step:

>3->2->1 | 4->5->6 | 7->8

>4->5->6 becomes 6->5->4

And we put it back into the list

>3->2->1 -> 6->5->4 -> 7->8

Third step:

We reach the end of the list before counting 3 nodes. That
means our job is done and we can return our list.

### Complexities:

- Time: O(n)
- Space: O(1)