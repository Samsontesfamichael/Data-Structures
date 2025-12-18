"""
AVL Tree Implementation (Self-Balancing Binary Search Tree)
Time Complexity:
- Insertion: O(log n)
- Deletion: O(log n)
- Searching: O(log n)
- All operations maintain O(log n) due to balancing
"""

class AVLNode:
    """Node class for AVL tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height of node

class AVLTree:
    """AVL Tree with self-balancing operations"""
    
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        """Get height of node - O(1)"""
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Get balance factor of node - O(1)"""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node):
        """Update height of node - O(1)"""
        if not node:
            return
        node.height = 1 + max(self._get_height(node.left), 
                             self._get_height(node.right))
    
    # 7.1 Tree Rotations
    def _rotate_right(self, z):
        """Right rotation - O(1)"""
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _rotate_left(self, z):
        """Left rotation - O(1)"""
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    # 7.2 Tree Rebalancing
    def _rebalance(self, node):
        """Rebalance node if needed - O(1)"""
        # Update height
        self._update_height(node)
        
        # Get balance factor
        balance = self._get_balance(node)
        
        # Left-Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Right-Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Left-Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right-Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    # 7.3 Insertion
    def insert(self, data):
        """Insert a new node - O(log n)"""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper for recursive insertion with balancing"""
        # Standard BST insertion
        if not node:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else:
            # Duplicate values not allowed
            return node
        
        # Rebalance the node
        return self._rebalance(node)
    
    # 7.4 Deletion
    def delete(self, data):
        """Delete a node - O(log n)"""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Helper for recursive deletion with balancing"""
        if not node:
            return node
        
        # Standard BST deletion
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            # Get inorder successor (smallest in right subtree)
            min_node = self._find_min_node(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(node.right, min_node.data)
        
        # Rebalance the node
        return self._rebalance(node)
    
    def _find_min_node(self, node):
        """Find node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current
    
    # Search operations
    def search(self, data):
        """Search for a value - O(log n)"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper for recursive search"""
        if not node or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)
    
    def contains(self, data):
        """Check if tree contains a value"""
        return self.search(data) is not None
    
    # Traversals
    def inorder_traversal(self):
        """Inorder traversal - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Preorder traversal - O(n)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    # Tree properties
    def get_height(self):
        """Get height of tree - O(1)"""
        return self._get_height(self.root)
    
    def is_balanced(self):
        """Check if tree is balanced - O(n)"""
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        """Helper to check if tree is balanced"""
        if not node:
            return True
        
        balance = self._get_balance(node)
        
        if abs(balance) > 1:
            return False
        
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))
    
    def find_min(self):
        """Find minimum value - O(log n)"""
        if not self.root:
            return None
        node = self._find_min_node(self.root)
        return node.data
    
    def find_max(self):
        """Find maximum value - O(log n)"""
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def is_empty(self):
        """Check if tree is empty"""
        return self.root is None
    
    def display_tree(self, node=None, level=0, prefix="Root: "):
        """Display tree structure"""
        if node is None:
            node = self.root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data) + 
                  f" (h={node.height}, b={self._get_balance(node)})")
            if node.left or node.right:
                if node.left:
                    self.display_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.display_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# Example usage and testing
if __name__ == "__main__":
    print("=== AVL Tree Demo ===\n")
    
    avl = AVLTree()
    
    # Insertion with automatic balancing
    print("1. Insertion Operations (with auto-balancing):")
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avl.insert(val)
        print(f"\nAfter inserting {val}:")
        avl.display_tree()
    
    print("\n2. Tree Properties:")
    print(f"Height: {avl.get_height()}")
    print(f"Is balanced: {avl.is_balanced()}")
    print(f"Min value: {avl.find_min()}")
    print(f"Max value: {avl.find_max()}")
    
    print("\n3. Traversals:")
    print(f"Inorder: {avl.inorder_traversal()}")
    print(f"Preorder: {avl.preorder_traversal()}")
    
    print("\n4. Search Operations:")
    print(f"Contains 25: {avl.contains(25)}")
    print(f"Contains 100: {avl.contains(100)}")
    
    print("\n5. Deletion Operations (with auto-balancing):")
    avl.delete(20)
    print(f"\nAfter deleting 20:")
    avl.display_tree()
    print(f"Inorder: {avl.inorder_traversal()}")
    print(f"Is balanced: {avl.is_balanced()}")
    
    # Demonstrate balancing with sequential insertions
    print("\n\n6. Demonstrating Auto-Balancing:")
    print("Inserting 1-7 sequentially (would create unbalanced BST):")
    avl2 = AVLTree()
    for i in range(1, 8):
        avl2.insert(i)
    
    print("\nResulting AVL Tree (balanced):")
    avl2.display_tree()
    print(f"Height: {avl2.get_height()} (vs {7} for unbalanced BST)")
    print(f"Is balanced: {avl2.is_balanced()}")
