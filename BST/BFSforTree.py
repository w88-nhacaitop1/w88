""" BFS Binary Tree

        1
      /   \
     2     3
   /   \
  4     5

*Breadth First Traversal:
    LevelOrder Traversal  : 1 2 3 4 5"""


import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def levelOrder1(self, root: TreeNode):
        if root is None:
            return None

        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    def levelOrder2(self, root: TreeNode):
        levels = []

        def helper(node, level):
            if node:
                if len(levels) == level:
                    levels.append([])

                levels[level] += [node.val]

                helper(node.left, level+1)
                helper(node.right, level+1)

        helper(root, 0)
        return levels


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s = Solution()
    print("Level Order: ", end=" ")
    s.levelOrder1(root)
