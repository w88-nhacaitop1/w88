""" 206. Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both? """

# TODO: Approach 1: Iterative           [O(n) & O(1)] 
# TODO: Approach 2: Recursive           [O(n) & O(n)]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr is not None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp

        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        return ListNode(0)
        

    def printList(self, node: ListNode):
        while node is not None:
            print(node.val, end="->")
            node = node.next
        print("NULL")
        
if __name__ == "__main__":
    # 1->2->3->4->5->NULL
    l1 = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    l1.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    s = Solution()
    s.printList(l1)

    reverseList = s.reverseList1(l1)

    s.printList(reverseList)
