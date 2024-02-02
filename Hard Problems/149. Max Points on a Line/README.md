## 149. Max Points on a Line

link: https://leetcode.com/problems/max-points-on-a-line/description/

### Problem:

Given an array of points where points[i] = [xi, yi] represents 
a point on the X-Y plane, return the maximum number of points 
that lie on the same straight line.

### Constraints:

- 1 <= points.length <= 300
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique.

### Discussing Solution:

We can do this by counting slopes. For each point we count
frequency of slopes of that point and all point after that point.
We don't need to calculate points that come before our point because
we already counted that slope before. If maximum frequency 
is bigger than our current maximum, we update it.

### Complexities:

- Time: O(n^2)
- Space: O(n)