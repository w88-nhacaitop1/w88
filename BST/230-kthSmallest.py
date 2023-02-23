""" 230. Kth Smallest Element in a BST (Medium)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

!Note:
!You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

*Input: root = [3, 1, 4, null, 2], k = 1
   3
  / \
 1   4
  \
   2
*Output: 1

*Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
*Output: 3

?Follow up:
?What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
?How would you optimize the kthSmallest routine?
 """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, inorder = [], float('-inf')

        while (stack or root) and k > 0:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            inorder = root.val
            root = root.right

            k -= 1

        return inorder


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    k = 3

    s = Solution()
    result = s.kthSmallest(root, k)

    print("Result is {}".format(result))
