""" 993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins. """

#         1
#       /   \
#      2     3
#        \     \
#         4     5

""" Depth First Traversals: """
# *   Preorder Traversal  : 1 2 4 3 5
# *   InOrder Traversal   : 4 2 5 1 3
# *   Postorder Traversal : 4 5 2 3 1




import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins1(self, root: TreeNode, x: int, y: int) -> bool:
        depth, parent = {}, {}

        def preOrder(node: TreeNode, parentNode: TreeNode):
            if node:
                depth[node.val] = depth[parentNode.val] + \
                    1 if parentNode else 0
                parent[node.val] = parentNode.val if parentNode else None

                preOrder(node.left, node)
                preOrder(node.right, node)

        preOrder(root, None)

        return depth[x] == depth[y] and parent[x] != parent[y]

    def isCousins2(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([(root, None)])
        x_parent, y_parent = None, None

        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue += [(node.left, node)]
                if node.right:
                    queue += [(node.right, node)]

            if x_parent or y_parent:
                if x_parent and y_parent and x_parent is not y_parent:
                    return True
                return False

        return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    s = Solution()
    result1 = s.isCousins1(root, 4, 5)
    result2 = s.isCousins2(root, 4, 5)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
