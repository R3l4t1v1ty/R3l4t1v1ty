import typing
from typing import List
from typing import Optional
import math
import functools
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_list(head: Optional[ListNode]) -> List[Optional[ListNode]]:

            c = head
            prev = None
            nxt = None
            while c:
                nxt = c.next
                c.next = prev
                prev = c
                c = nxt

            return [prev, head]

        if not head or not head.next:
            return head
        if k == 1:
            return head
        lleft = None
        left = head
        right = head.next

        i = 2
        while right:
            if i == k:
                if lleft:
                    lleft.next = None
                rright = right.next
                right.next = None
                pom1, pom2 = reverse_list(left)
                if lleft:
                    lleft.next = pom1
                else:
                    head = pom1
                pom2.next = rright
                lleft = pom2
                left = lleft.next
                if rright:
                    right = rright.next
                else:
                    right = None
                i = 2
            else:
                right = right.next
                i += 1

        return head

def main():
    l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8))))))))
    head = Solution.reverseKGroup(None,l1,3)
    pom = head
    arr = []
    while pom:
        arr.append(pom.val)
        pom = pom.next
    print(arr)
    exit()

if __name__ == "__main__":
    main()