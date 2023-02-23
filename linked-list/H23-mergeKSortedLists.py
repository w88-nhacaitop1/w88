""" 23. Merge K Sorted List (Hard)
https://leetcode.com/problems/merge-k-sorted-lists/

Merge K sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6 """

# TODO: Approach 1: Using Min Heap          [O(nk logk) & O(k)]
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/486481/Python-Using-Min-Heap

from typing import List
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for l in lists:
            while(l):
                heapq.heappush(heap, l.val)
                l = l.next

        tmp = ListNode(-1)
        curr = tmp
        while(heap):
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return tmp.next

    def print_list(self, node: ListNode):
        p = node
        while p is not None:
            print(p.val, end="->")
            p = p.next

        print("NULL")


if __name__ == "__main__":
    # list = [[1, 4, 5], [1, 3, 4], [2, 6]]

    llist1 = ListNode(1)
    second1 = ListNode(4)
    third1 = ListNode(5)
    llist1.next = second1
    second1.next = third1

    llist2 = ListNode(1)
    second2 = ListNode(3)
    third2 = ListNode(4)
    llist2.next = second2
    second2.next = third2

    llist3 = ListNode(2)
    second3 = ListNode(6)
    llist3.next = second3

    data = [llist1, llist2, llist3]

    s = Solution()
    s.print_list(s.mergeKLists(data))
