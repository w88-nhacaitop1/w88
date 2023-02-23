# DFS Binary Tree

#         1
#       /   \
#      2     3
#    /   \
#   4     5

# Depth First Traversals:
#   Preorder Traversal  : 1 2 4 5 3
#   InOrder Traversal   : 4 2 5 1 3
#   Postorder Traversal : 4 5 2 3 1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrder(root: TreeNode):
    if root:
        print(root.val, end=" ")
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root: TreeNode):
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)


def postOrder(root: TreeNode):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val, end=" ")


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("PreOrder: ", end=" ")
    preOrder(root)
    print("\nInOrder: ", end=" ")
    inOrder(root)
    print("\nPostOrder: ", end=" ")
    postOrder(root)
    print("\n")
