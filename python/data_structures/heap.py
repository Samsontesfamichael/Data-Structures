"""
Min Heap Implementation
Time Complexity:
- Insertion: O(log n)
- Deletion (extract min): O(log n)
- Searching: O(n)
- Get min: O(1)
"""

class MinHeap:
    """Min Heap implementation using array"""
    
    def __init__(self):
        self.heap = []
    
    def _parent_index(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def _right_child_index(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def _has_parent(self, index):
        """Check if node has parent"""
        return self._parent_index(index) >= 0
    
    def _has_left_child(self, index):
        """Check if node has left child"""
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        """Check if node has right child"""
        return self._right_child_index(index) < len(self.heap)
    
    def _parent(self, index):
        """Get parent value"""
        return self.heap[self._parent_index(index)]
    
    def _left_child(self, index):
        """Get left child value"""
        return self.heap[self._left_child_index(index)]
    
    def _right_child(self, index):
        """Get right child value"""
        return self.heap[self._right_child_index(index)]
    
    def _swap(self, index1, index2):
        """Swap two elements in heap"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    # 4.1 Insertion
    def insert(self, value):
        """Insert a new value into heap - O(log n)"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, index):
        """Maintain heap property by moving element up"""
        while self._has_parent(index) and self._parent(index) > self.heap[index]:
            parent_idx = self._parent_index(index)
            self._swap(index, parent_idx)
            index = parent_idx
    
    # 4.2 Deletion (Extract Min)
    def extract_min(self):
        """Remove and return the minimum element - O(log n)"""
        if not self.heap:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_value
    
    def delete(self, value):
        """Delete a specific value from heap - O(n)"""
        try:
            index = self.heap.index(value)
        except ValueError:
            return False
        
        # Replace with last element
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        
        # Heapify
        if index < len(self.heap):
            self._heapify_down(index)
            self._heapify_up(index)
        
        return True
    
    def _heapify_down(self, index):
        """Maintain heap property by moving element down"""
        while self._has_left_child(index):
            smaller_child_idx = self._left_child_index(index)
            
            if (self._has_right_child(index) and 
                self._right_child(index) < self._left_child(index)):
                smaller_child_idx = self._right_child_index(index)
            
            if self.heap[index] < self.heap[smaller_child_idx]:
                break
            
            self._swap(index, smaller_child_idx)
            index = smaller_child_idx
    
    # 4.3 Searching
    def search(self, value):
        """Search for a value in heap - O(n)"""
        try:
            index = self.heap.index(value)
            return index
        except ValueError:
            return -1
    
    def contains(self, value):
        """Check if heap contains a value - O(n)"""
        return value in self.heap
    
    def peek(self):
        """Get the minimum element without removing - O(1)"""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    # 4.4 Traversal
    def get_all_elements(self):
        """Get all elements in heap array order - O(n)"""
        return self.heap.copy()
    
    def get_sorted_elements(self):
        """Get all elements in sorted order (destroys heap) - O(n log n)"""
        sorted_list = []
        temp_heap = self.heap.copy()
        
        while self.heap:
            sorted_list.append(self.extract_min())
        
        self.heap = temp_heap
        return sorted_list
    
    def level_order_traversal(self):
        """Level order traversal (same as array order for heap)"""
        return self.heap.copy()
    
    def size(self):
        """Get the size of heap - O(1)"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty - O(1)"""
        return len(self.heap) == 0
    
    def build_heap(self, array):
        """Build heap from array - O(n)"""
        self.heap = array.copy()
        # Start from last non-leaf node and heapify down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def display(self):
        """Display heap structure"""
        if not self.heap:
            print("Heap is empty")
            return
        
        print(f"Heap array: {self.heap}")
        print(f"Min element: {self.peek()}")
        
        # Display as tree structure
        height = 0
        level_size = 1
        index = 0
        
        while index < len(self.heap):
            level = []
            for i in range(level_size):
                if index < len(self.heap):
                    level.append(str(self.heap[index]))
                    index += 1
            print(f"Level {height}: {' '.join(level)}")
            height += 1
            level_size *= 2


# Example usage and testing
if __name__ == "__main__":
    print("=== Min Heap Demo ===\n")
    
    # Create a new min heap
    heap = MinHeap()
    
    # Insertion
    print("1. Insertion Operations:")
    values = [50, 30, 20, 15, 10, 8, 16, 25, 40, 12]
    for val in values:
        heap.insert(val)
    print(f"Inserted values: {values}")
    heap.display()
    
    # Peek
    print(f"\n2. Peek (min element): {heap.peek()}")
    
    # Searching
    print("\n3. Searching Operations:")
    print(f"Search for 15: Found at index {heap.search(15)}")
    print(f"Search for 100: Found at index {heap.search(100)}")
    print(f"Contains 20: {heap.contains(20)}")
    
    # Extract min
    print("\n4. Extract Min Operations:")
    print(f"Extract min: {heap.extract_min()}")
    print(f"Extract min: {heap.extract_min()}")
    print("After extracting min twice:")
    heap.display()
    
    # Delete specific value
    print("\n5. Delete Specific Value:")
    heap.delete(30)
    print("After deleting 30:")
    heap.display()
    
    # Traversal
    print("\n6. Traversal:")
    print(f"Level order: {heap.level_order_traversal()}")
    print(f"Sorted order: {heap.get_sorted_elements()}")
    
    # Build heap from array
    print("\n7. Build Heap from Array:")
    new_heap = MinHeap()
    new_heap.build_heap([45, 20, 14, 12, 31, 7, 11, 13, 7])
    print("Built heap from [45, 20, 14, 12, 31, 7, 11, 13, 7]:")
    new_heap.display()
    
    # Properties
    print(f"\n8. Heap Properties:")
    print(f"Size: {heap.size()}")
    print(f"Is empty: {heap.is_empty()}")
