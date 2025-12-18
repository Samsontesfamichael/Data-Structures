"""
Doubly Linked List Implementation
Time Complexity:
- Insertion: O(1) at head/tail, O(n) at specific position
- Deletion: O(n)
- Traversal: O(n)
"""

class DNode:
    """Node class for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Doubly Linked List with common operations"""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    # 2.2.1 Insertion
    def insert_at_beginning(self, data):
        """Insert node at the beginning - O(1)"""
        new_node = DNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert node at the end - O(1)"""
        new_node = DNode(data)
        
        if not self.tail:
            self.head = self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def insert_at_position(self, data, position):
        """Insert node at specific position - O(n)"""
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = DNode(data)
        current = self.head
        
        for i in range(position - 1):
            if not current:
                print("Position out of bounds")
                return
            current = current.next
        
        if not current:
            print("Position out of bounds")
            return
        
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node
        
        current.next = new_node
    
    def insert_after_node(self, target_data, data):
        """Insert after a specific node value - O(n)"""
        current = self.head
        
        while current:
            if current.data == target_data:
                new_node = DNode(data)
                new_node.next = current.next
                new_node.prev = current
                
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                
                current.next = new_node
                return
            current = current.next
        
        print(f"Node with data {target_data} not found")
    
    # 2.2.2 Deletion
    def delete_by_value(self, key):
        """Delete first node with given value - O(n)"""
        if not self.head:
            return
        
        current = self.head
        
        while current:
            if current.data == key:
                # Node to delete is head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                # Node to delete is tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                # Node to delete is in middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
    
    def delete_at_position(self, position):
        """Delete node at specific position - O(n)"""
        if not self.head:
            return
        
        current = self.head
        
        for i in range(position):
            if not current:
                print("Position out of bounds")
                return
            current = current.next
        
        if not current:
            print("Position out of bounds")
            return
        
        # Delete head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        # Delete tail
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = None
        # Delete middle node
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
    
    def delete_first(self):
        """Delete the first node - O(1)"""
        if not self.head:
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def delete_last(self):
        """Delete the last node - O(1)"""
        if not self.tail:
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    # Traversal
    def traverse_forward(self):
        """Traverse forward and return elements - O(n)"""
        elements = []
        current = self.head
        
        while current:
            elements.append(current.data)
            current = current.next
        
        return elements
    
    # 2.2.3 Reverse Traversal
    def traverse_backward(self):
        """Traverse backward and return elements - O(n)"""
        elements = []
        current = self.tail
        
        while current:
            elements.append(current.data)
            current = current.prev
        
        return elements
    
    def display_forward(self):
        """Display the list forward"""
        elements = self.traverse_forward()
        print("None <- " + " <-> ".join(map(str, elements)) + " -> None")
    
    def display_backward(self):
        """Display the list backward"""
        elements = self.traverse_backward()
        print("None <- " + " <-> ".join(map(str, elements)) + " -> None")
    
    def search(self, key):
        """Search for a node with given key - O(n)"""
        current = self.head
        position = 0
        
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        
        return -1
    
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
    print("=== Doubly Linked List Demo ===\n")
    
    # Create a new doubly linked list
    dll = DoublyLinkedList()
    
    # Insertion operations
    print("1. Insertion Operations:")
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(1)
    print("After inserting 1, 2, 3 at beginning:")
    dll.display_forward()
    
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    print("After inserting 4, 5 at end:")
    dll.display_forward()
    
    dll.insert_at_position(3.5, 3)
    print("After inserting 3.5 at position 3:")
    dll.display_forward()
    
    dll.insert_after_node(3, 3.2)
    print("After inserting 3.2 after node with value 3:")
    dll.display_forward()
    
    # Deletion operations
    print("\n2. Deletion Operations:")
    dll.delete_by_value(3.2)
    print("After deleting value 3.2:")
    dll.display_forward()
    
    dll.delete_at_position(3)
    print("After deleting at position 3:")
    dll.display_forward()
    
    dll.delete_first()
    print("After deleting first node:")
    dll.display_forward()
    
    dll.delete_last()
    print("After deleting last node:")
    dll.display_forward()
    
    # Traversal operations
    print("\n3. Traversal Operations:")
    print(f"Forward traversal: {dll.traverse_forward()}")
    print(f"Backward traversal: {dll.traverse_backward()}")
    
    print("\nDisplay backward:")
    dll.display_backward()
    
    # Other operations
    print("\n4. Other Operations:")
    print(f"Search for 3: Found at position {dll.search(3)}")
    print(f"Length of list: {dll.get_length()}")
    print(f"Is empty: {dll.is_empty()}")
