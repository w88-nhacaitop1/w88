""" 1008. Construct Binary Search Tree from Preorder Traversal (Medium)
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
https://leetcode.com/articles/construct-bst-from-preorder-traversal/

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,
and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first,
then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

*Input: [8,5,1,7,10,12]
*Output: [8,5,10,1,7,null,12]

!Constraints:
!   1 <= preorder.length <= 100
!   1 <= preorder[i] <= 10^8
!The values of preorder are distinct.
 """

# TODO: Approach 1: Using Inorder to construct BST          [O(NlogN) & O(N)]
# TODO: Approach 2: Using Recursion                         [O(N) & O(N)]
# TODO: Approach 3: Using Iteration & stack                 [O(N) & O(N)]

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder1(self, preorder: List[int]) -> TreeNode:
        def helper(left=0, right=len(preorder)):
            nonlocal pre_idx
            # ? if there is no elements to construct subtrees
            if left == right:
                return None

            # ? pick up pre_idx element as a root
            rootVal = preorder[pre_idx]
            root = TreeNode(rootVal)

            # ? root splits inorder list
            # ? into left and right subtrees
            index = hashTable[rootVal]

            pre_idx += 1
            root.left = helper(left, index)             # ? left = 0; right = 3
            root.right = helper(index + 1, right)       # ? left = 4; right = 6
            return root

        # ? sort array
        inorder = sorted(preorder)
        # ? start from first preorder element
        pre_idx = 0
        # ? build a hashmap value -> its index
        hashTable = {val: idx for idx, val in enumerate(inorder)}
        return helper()

    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            # ? if all elements from preorder are used
            # ? then the tree is constructed
            if idx == n:
                return None

            val = preorder[idx]
            # ? if the current element
            # ? couldn't be placed here to meet BST requirements
            if val < lower or val > upper:
                return None

            # ? place the current element
            # ? and recursively construct subtrees
            idx += 1
            root = TreeNode(val)
            print(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()


if __name__ == "__main__":
    preorder = [8, 5, 1, 7, 10, 12]  # ? Output = [8,5,10,1,7,null,12]

    s = Solution()
    result1 = s.bstFromPreorder1(preorder)
    result2 = s.bstFromPreorder2(preorder)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
