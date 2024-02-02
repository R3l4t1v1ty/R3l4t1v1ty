import typing
from typing import List
from typing import Optional
import math
import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxv = [-10000000000]

        def fun(rt):
            if not rt:
                return 0

            a = fun(rt.left)
            b = fun(rt.right)

            maxv[0] = max(maxv[0], a + b + rt.val, a + rt.val, b + rt.val, rt.val)

            return max(a, b, 0) + rt.val

        a = fun(root)

        return max(maxv[0], a)

def main():
    tree = TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    res = Solution.maxPathSum(None,tree)
    print(res)
    exit()

if __name__ == "__main__":
    main()