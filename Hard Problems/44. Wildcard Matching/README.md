## 42. Wildcard Matching

link: https://leetcode.com/problems/wildcard-matching/description/

### Problem:

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

### Constraints:

- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters.
- p contains only lowercase English letters, '?' or '*'.

### Discussing Solution:

We are going to use recursion for this one.
We have 2 pointers (***si***,***pi***), one pointing at the current character in
the string ***s*** and one pointing at the current character 
in the string ***p***. 

Now we take a look at ***p[pi]***, if it is "*" or if it is "?" or the 
same character as ***s[si]***.

In the first case, we have to recursively check if any of the
following match (si,pi+1), (si+1,pi), (si+1,pi+1).

In the second case, we have to recursively check if (si+1,pi+1)
match.

### Complexities:

- Time: O(n*m)
- Space: O(n*m)
- m and n are sizes of strings p and s