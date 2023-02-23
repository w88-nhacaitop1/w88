""" 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. """

# TODO: Define sum = x + y + carry, carry = sum//10

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        p = l1
        q = l2

        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = x + y + carry
            carry = sum//10
            current.next = ListNode(sum%10)
            current = current.next

            p = p.next if p != None else None
            q = q.next if q != None else None

        if carry > 0:
            current.next = ListNode(carry)

        return dummyHead.next

    def print_list(self, node: ListNode):
        while node is not None:
            print(node.val, end=" ")
            node = node.next


if __name__ == "__main__":
    llist1 = ListNode(2)
    second = ListNode(4)
    third = ListNode(3)
    llist1.next = second
    second.next = third

    llist2 = ListNode(5)
    second2 = ListNode(6)
    third2 = ListNode(4)
    llist2.next = second2
    second2.next = third2

    s = Solution()
    result = s.addTwoNumbers(llist1, llist2)

    s.print_list(result)
