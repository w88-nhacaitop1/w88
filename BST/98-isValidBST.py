""" 98. Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/
https://leetcode.com/articles/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

*Example 1:
    2
   / \
  1   3
*Input: [2,1,3]
*Output: true

*Example 2:
    5
   / \
  1   4
     / \
    3   6
*Input: [5,1,4,null,null,3,6]
*Output: false
*Explanation: The root node's value is 5 but its right child's value is 4.
 """

# TODO: Approach 1: Recursion
# TODO: Approach 2: Iteration
# TODO: Approach 3: Depth First Search using stack          [O(N) & O(N)]

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False

            inorder = root.val
            root = root.right

        return True


if __name__ == "__main__":
    arr = [2, 1, 3]
    # arr = [3, 1, 5, None, None, 4, 6]
    # arr = [5, 1, 4, None, None, 3, 6]
    arr = [5, 1, 4, None, None, 3, 6]

    # node = TreeNode(arr[0])
    # node.left = TreeNode(arr[1])
    # node.right = TreeNode(arr[2])
    # node.right.left = TreeNode(arr[5])
    # node.right.right = TreeNode(arr[6])

    s = Solution()
    print(s.isValidBST(arr))
