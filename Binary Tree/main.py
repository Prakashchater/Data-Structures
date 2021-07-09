class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preOrder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inOrder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postOrder(tree.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")
            return False

    def preOrder(self, start, traversal):
        """ Root->Left->Right """
        """1-2-4-5-3-6-7-"""
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preOrder(start.left, traversal)
            traversal = self.preOrder(start.right, traversal)
        return traversal

    def inOrder(self, start, traversal):
        """ Left->Root->Right """
        """4-2-5-1-6-3-7-"""
        if start:
            traversal = self.inOrder(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inOrder(start.right, traversal)
        return traversal

    def postOrder(self, start, traversal):
        """ Left->Right->Root """
        """4-2-5-6-3-7-1-"""
        if start:
            traversal = self.inOrder(start.left, traversal)
            traversal = self.inOrder(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal

# 1-2-4-5-3-6-7-8-9-       PreOrder
# 4-2-5-1-6-3-8-7-9-       InOrder
# 4-2-5-6-3-8-7-9-1-       PostOrder
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(8)
tree.root.right.right.right = Node(9)
tree.root.right.left.right = Node(9)
tree.root.right.left.left = Node(9)

print("PreOrder Traversal ")
print(tree.printTree("preorder"))
print("\nInOrder Traversal")
print(tree.printTree("inorder"))
print("\nPostOrder Traversal")
print(tree.printTree("postorder"))