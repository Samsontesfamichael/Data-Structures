"""
Binary Search Tree Implementation
Time Complexity:
- Insertion: O(log n) average, O(n) worst case
- Searching: O(log n) average, O(n) worst case
- Deletion: O(log n) average, O(n) worst case
- Traversals: O(n)
"""

from collections import deque

class TreeNode:
    """Node class for binary search tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree with common operations"""
    
    def __init__(self):
        self.root = None
    
    # 3.1 Insertion
    def insert(self, data):
        """Insert a new node - O(log n) average"""
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for recursive insertion"""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
        # If data == node.data, we don't insert duplicates
    
    # 3.2 Searching
    def search(self, key):
        """Search for a key in the tree - O(log n) average"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """Helper method for recursive search"""
        if node is None or node.data == key:
            return node
        
        if key < node.data:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def contains(self, key):
        """Check if tree contains a key"""
        return self.search(key) is not None
    
    # 3.3 Deletion
    def delete(self, key):
        """Delete a node with given key - O(log n) average"""
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        """Helper method for recursive deletion"""
        if node is None:
            return node
        
        # Find the node to delete
        if key < node.data:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.data:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Get the inorder successor (smallest in the right subtree)
            min_node = self._find_min_node(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(node.right, min_node.data)
        
        return node
    
    def _find_min_node(self, node):
        """Find the node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current
    
    # 3.4 Finding the parent of a given node
    def find_parent(self, key):
        """Find the parent of a node with given key - O(log n) average"""
        return self._find_parent_recursive(self.root, None, key)
    
    def _find_parent_recursive(self, node, parent, key):
        """Helper method for finding parent"""
        if node is None:
            return None
        
        if node.data == key:
            return parent
        
        if key < node.data:
            return self._find_parent_recursive(node.left, node, key)
        else:
            return self._find_parent_recursive(node.right, node, key)
    
    # 3.5 Attaining a reference to a node
    def get_node(self, key):
        """Get reference to a node with given key"""
        return self.search(key)
    
    # 3.6 Finding the smallest and largest values
    def find_min(self):
        """Find the minimum value in the tree - O(log n) average"""
        if not self.root:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self):
        """Find the maximum value in the tree - O(log n) average"""
        if not self.root:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    # 3.7 Tree Traversals
    
    # 3.7.1 Preorder (Root -> Left -> Right)
    def preorder_traversal(self):
        """Preorder traversal - O(n)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper for preorder traversal"""
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    # 3.7.2 Postorder (Left -> Right -> Root)
    def postorder_traversal(self):
        """Postorder traversal - O(n)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper for postorder traversal"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    # 3.7.3 Inorder (Left -> Root -> Right) - gives sorted order
    def inorder_traversal(self):
        """Inorder traversal - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    # 3.7.4 Breadth First (Level Order)
    def breadth_first_traversal(self):
        """Breadth-first (level-order) traversal - O(n)"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def get_height(self):
        """Get the height of the tree - O(n)"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper for calculating height"""
        if node is None:
            return 0
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def is_empty(self):
        """Check if tree is empty"""
        return self.root is None
    
    def count_nodes(self):
        """Count total number of nodes - O(n)"""
        return self._count_recursive(self.root)
    
    def _count_recursive(self, node):
        """Helper for counting nodes"""
        if node is None:
            return 0
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)


# Example usage and testing
if __name__ == "__main__":
    print("=== Binary Search Tree Demo ===\n")
    
    # Create a new BST
    bst = BinarySearchTree()
    
    # Insertion
    print("1. Insertion Operations:")
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
    for val in values:
        bst.insert(val)
    print(f"Inserted values: {values}")
    
    # Searching
    print("\n2. Searching Operations:")
    print(f"Search for 40: {'Found' if bst.search(40) else 'Not found'}")
    print(f"Search for 100: {'Found' if bst.search(100) else 'Not found'}")
    print(f"Contains 60: {bst.contains(60)}")
    
    # Min and Max
    print("\n3. Finding Min and Max:")
    print(f"Minimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    
    # Parent finding
    print("\n4. Finding Parent:")
    parent = bst.find_parent(40)
    print(f"Parent of 40: {parent.data if parent else 'None (root)'}")
    parent = bst.find_parent(50)
    print(f"Parent of 50: {parent.data if parent else 'None (root)'}")
    
    # Traversals
    print("\n5. Tree Traversals:")
    print(f"Preorder:  {bst.preorder_traversal()}")
    print(f"Inorder:   {bst.inorder_traversal()}")
    print(f"Postorder: {bst.postorder_traversal()}")
    print(f"Breadth-first: {bst.breadth_first_traversal()}")
    
    # Tree properties
    print("\n6. Tree Properties:")
    print(f"Height: {bst.get_height()}")
    print(f"Total nodes: {bst.count_nodes()}")
    
    # Deletion
    print("\n7. Deletion Operations:")
    print(f"Before deletion: {bst.inorder_traversal()}")
    bst.delete(20)
    print(f"After deleting 20: {bst.inorder_traversal()}")
    bst.delete(30)
    print(f"After deleting 30: {bst.inorder_traversal()}")
    bst.delete(50)
    print(f"After deleting 50 (root): {bst.inorder_traversal()}")
