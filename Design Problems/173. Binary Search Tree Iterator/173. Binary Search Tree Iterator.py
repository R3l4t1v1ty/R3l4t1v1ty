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


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.stack = [root]
        self.fill_left()

    def fill_left(self):
        pom = self.stack[-1].left

        while pom:
            self.stack.append(pom)
            pom = pom.left

    def next(self) -> int:
        pom = self.stack.pop(-1)
        if pom.right:
            self.stack.append(pom.right)
            self.fill_left()
        return pom.val

    def hasNext(self) -> bool:
        return len(self.stack)


def main():
    tree = TreeNode(7,TreeNode(3),TreeNode(15,TreeNode(9),TreeNode(20)))
    obj = BSTIterator(tree)

    while obj.hasNext():
        print(obj.next())

    exit()

if __name__ == "__main__":
    main()