"""
Singly Linked List Implementation
Time Complexity:
- Insertion: O(1) at head, O(n) at tail or specific position
- Searching: O(n)
- Deletion: O(n)
- Traversal: O(n)
"""

class Node:
    """Node class for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly Linked List with common operations"""
    
    def __init__(self):
        self.head = None
    
    # 2.1.1 Insertion
    def insert_at_beginning(self, data):
        """Insert node at the beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert node at the end - O(n)"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, data, position):
        """Insert node at specific position - O(n)"""
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for i in range(position - 1):
            if not current:
                print("Position out of bounds")
                return
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    # 2.1.2 Searching
    def search(self, key):
        """Search for a node with given key - O(n)"""
        current = self.head
        position = 0
        
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
    
    def contains(self, key):
        """Check if list contains a key - O(n)"""
        return self.search(key) != -1
    
    # 2.1.3 Deletion
    def delete_by_value(self, key):
        """Delete first node with given value - O(n)"""
        if not self.head:
            return
        
        # If head needs to be deleted
        if self.head.data == key:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
    
    def delete_at_position(self, position):
        """Delete node at specific position - O(n)"""
        if not self.head:
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(position - 1):
            if not current.next:
                print("Position out of bounds")
                return
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    # 2.1.4 Traversing the list
    def traverse(self):
        """Traverse and print all elements - O(n)"""
        elements = []
        current = self.head
        
        while current:
            elements.append(current.data)
            current = current.next
        
        return elements
    
    def display(self):
        """Display the linked list"""
        elements = self.traverse()
        print(" -> ".join(map(str, elements)) + " -> None")
    
    # 2.1.5 Traversing the list in reverse order
    def reverse_traverse_recursive(self, node=None):
        """Traverse in reverse using recursion - O(n)"""
        if node is None:
            node = self.head
        
        if node is None:
            return []
        
        if node.next is None:
            return [node.data]
        
        return self.reverse_traverse_recursive(node.next) + [node.data]
    
    def reverse(self):
        """Reverse the linked list - O(n)"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def get_length(self):
        """Get the length of the list - O(n)"""
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None


# Example usage and testing
if __name__ == "__main__":
    print("=== Singly Linked List Demo ===\n")
    
    # Create a new linked list
    sll = SinglyLinkedList()
    
    # Insertion operations
    print("1. Insertion Operations:")
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    print("After inserting 1, 2, 3 at beginning:")
    sll.display()
    
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    print("After inserting 4, 5 at end:")
    sll.display()
    
    sll.insert_at_position(2.5, 2)
    print("After inserting 2.5 at position 2:")
    sll.display()
    
    # Searching operations
    print("\n2. Searching Operations:")
    print(f"Search for 3: Found at position {sll.search(3)}")
    print(f"Search for 10: Found at position {sll.search(10)}")
    print(f"Contains 4: {sll.contains(4)}")
    print(f"Contains 100: {sll.contains(100)}")
    
    # Deletion operations
    print("\n3. Deletion Operations:")
    sll.delete_by_value(2.5)
    print("After deleting value 2.5:")
    sll.display()
    
    sll.delete_at_position(0)
    print("After deleting at position 0:")
    sll.display()
    
    # Traversal operations
    print("\n4. Traversal Operations:")
    print(f"Forward traversal: {sll.traverse()}")
    print(f"Reverse traversal: {sll.reverse_traverse_recursive()}")
    
    # Reverse the list
    print("\n5. Reversing the list:")
    sll.reverse()
    print("After reversing:")
    sll.display()
    
    # Other operations
    print("\n6. Other Operations:")
    print(f"Length of list: {sll.get_length()}")
    print(f"Is empty: {sll.is_empty()}")
