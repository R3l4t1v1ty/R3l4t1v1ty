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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]):

            if not list1 and not list2:
                return None
            if not list1:
                return list2
            if not list2:
                return list1

            head = None

            if list1 and list2:
                if list1.val < list2.val:
                    head = list1
                    list1 = list1.next
                else:
                    head = list2
                    list2 = list2.next

            curr = head

            while list1 and list2:
                if list1.val < list2.val:
                    pom = list1
                    list1 = list1.next
                    curr.next = pom
                    curr = curr.next
                else:
                    pom = list2
                    list2 = list2.next
                    curr.next = pom
                    curr = curr.next

            if list1:
                curr.next = list1
            elif list2:
                curr.next = list2

            return head

        def merge_sort(start: int, end: int) -> Optional[ListNode]:

            if start == end:
                return lists[start]

            mid = start + (end - start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)

            return merge_two_lists(left, right)

        k = len(lists)

        if not k:
            return None

        return merge_sort(0, k - 1)

def main():
    l1 = ListNode(1,ListNode(2,ListNode(3)))
    l2 = ListNode(2,ListNode(4,ListNode(6)))
    l3 = ListNode(3,ListNode(6,ListNode(12)))
    l4 = ListNode(4,ListNode(8,ListNode(16)))
    head = Solution.mergeKLists(None,[l1,l2,l3,l4])
    pom = head
    arr = []
    while pom:
        arr.append(pom.val)
        pom = pom.next
    print(arr)
    exit()

if __name__ == "__main__":
    main()