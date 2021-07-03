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
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")
            return False

    def preOrder(self, start, traversal):
        """ Root->Left->Right """
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preOrder(start.left, traversal)
            traversal = self.preOrder(start.right, traversal)
        return traversal

    def inOrder(self, start, traversal):
        pass

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.printTree("preorder"))