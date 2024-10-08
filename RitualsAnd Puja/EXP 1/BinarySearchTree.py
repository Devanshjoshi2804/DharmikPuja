class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

def main():
    bst = BST()
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        root = bst.insert(root, key)

    print("Inorder Traversal:")
    bst.inorder_traversal(root)

    # Search for a key
    search_key = 70
    result = bst.search(root, search_key)
    if result:
        print(f"\n{search_key} found in the BST.")
    else:
        print(f"\n{search_key} not found in the BST.")

if __name__ == "__main__":
    main()
