""" 21. Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->5, 1->3->4
Output: 1->1->2->3->4->5 """

# TODO: Approach 1: Recursion           [O(n+m) & O(n+m)]
# TODO: Approach 2: Iteration           [O(n+m) & O(1)]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists1(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        prev = dummyHead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            # Then, regardless of which list we connected,
            # we increment prev to keep it one step behind one of our list heads.
            prev = prev.next
            print("Head: {0}".format(self.print_list(dummyHead)))
            print("Prev: {0}\n".format(self.print_list(prev)))

        prev.next = l1 or l2

        return dummyHead.next

    def print_list(self, node: ListNode):
        p = node
        while p is not None:
            print(p.val, end=" ")
            p = p.next


if __name__ == "__main__":
    llist1 = ListNode(1)
    second = ListNode(2)
    third = ListNode(5)
    llist1.next = second
    second.next = third

    llist2 = ListNode(1)
    second2 = ListNode(3)
    third2 = ListNode(4)
    llist2.next = second2
    second2.next = third2

    s = Solution()
    result = s.mergeTwoLists1(llist1, llist2)
    # result = s.mergeTwoLists2(llist1, llist2)

    s.print_list(result)
