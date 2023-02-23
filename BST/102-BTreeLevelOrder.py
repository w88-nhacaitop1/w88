""" 102. Binary Tree Level Order Traversal (Medium)
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example: Given binary tree [3,9,20,null,null,15,7],

      3
     / \
    9  20
      /  \
    15    7

return its level order traversal as:
    [
      [3],
      [9, 20],
      [15, 7]
    ]
 """

# TODO: Approach 1: Using Iteration & Queue         [O(N) & O(N)]
# TODO: Approach 2: Using Recursion                 [O(N) & O(N)]

# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # TODO: Using Iteration & queue
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])

        while queue:
            levels.append([])
            levelLen = len(queue)

            for i in range(levelLen):
                node = queue.popleft()

                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return levels

    # TODO: Using Recursion
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def bfs(node: TreeNode, level: int):
            if node:
                if len(levels) == level:
                    levels.append([])

                levels[level] += [node.val]

                bfs(node.left, level+1)
                bfs(node.right, level+1)

        bfs(root, 0)

        return levels


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    result1 = s.levelOrder1(root)
    result2 = s.levelOrder2(root)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
