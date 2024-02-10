class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=' ')


tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

print("Inorder traversal:")
tree.inorder_traversal(tree.root)

print("\nPreorder traversal:")
tree.preorder_traversal(tree.root)

print("\nPostorder traversal:")
tree.postorder_traversal(tree.root)
