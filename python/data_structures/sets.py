"""
Set Implementations (Unordered and Ordered)
Time Complexity:
- Insertion: O(1) average for unordered, O(log n) for ordered
- Deletion: O(1) average for unordered, O(log n) for ordered
- Search: O(1) average for unordered, O(log n) for ordered
"""

class UnorderedSet:
    """Unordered Set implementation using hash table (Python set)"""
    
    def __init__(self):
        self.items = set()
    
    # 5.1.1 Insertion
    def add(self, item):
        """Add an item to the set - O(1) average"""
        self.items.add(item)
    
    def remove(self, item):
        """Remove an item from the set - O(1) average"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def discard(self, item):
        """Remove an item if present (no error if not found) - O(1) average"""
        self.items.discard(item)
    
    def contains(self, item):
        """Check if set contains an item - O(1) average"""
        return item in self.items
    
    def size(self):
        """Get the size of the set - O(1)"""
        return len(self.items)
    
    def is_empty(self):
        """Check if set is empty - O(1)"""
        return len(self.items) == 0
    
    def clear(self):
        """Remove all items from set - O(1)"""
        self.items.clear()
    
    def get_all(self):
        """Get all items as a list - O(n)"""
        return list(self.items)
    
    # Set operations
    def union(self, other_set):
        """Return union of two sets - O(n + m)"""
        result = UnorderedSet()
        result.items = self.items.union(other_set.items)
        return result
    
    def intersection(self, other_set):
        """Return intersection of two sets - O(min(n, m))"""
        result = UnorderedSet()
        result.items = self.items.intersection(other_set.items)
        return result
    
    def difference(self, other_set):
        """Return difference of two sets - O(n)"""
        result = UnorderedSet()
        result.items = self.items.difference(other_set.items)
        return result
    
    def is_subset(self, other_set):
        """Check if this set is a subset of another - O(n)"""
        return self.items.issubset(other_set.items)
    
    def is_superset(self, other_set):
        """Check if this set is a superset of another - O(m)"""
        return self.items.issuperset(other_set.items)
    
    def __str__(self):
        return f"{{{', '.join(map(str, sorted(self.items)))}}}"


class OrderedSet:
    """Ordered Set implementation using sorted list"""
    
    def __init__(self):
        self.items = []
    
    def _binary_search(self, item):
        """Binary search to find insertion point - O(log n)"""
        left, right = 0, len(self.items)
        
        while left < right:
            mid = (left + right) // 2
            if self.items[mid] < item:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    # 5.2 Ordered Set Operations
    def add(self, item):
        """Add an item maintaining order - O(n) due to insertion"""
        if item not in self.items:
            index = self._binary_search(item)
            self.items.insert(index, item)
    
    def remove(self, item):
        """Remove an item - O(n)"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def contains(self, item):
        """Check if set contains an item - O(log n)"""
        index = self._binary_search(item)
        return index < len(self.items) and self.items[index] == item
    
    def size(self):
        """Get the size of the set - O(1)"""
        return len(self.items)
    
    def is_empty(self):
        """Check if set is empty - O(1)"""
        return len(self.items) == 0
    
    def clear(self):
        """Remove all items from set - O(1)"""
        self.items.clear()
    
    def get_all(self):
        """Get all items in sorted order - O(1)"""
        return self.items.copy()
    
    def get_min(self):
        """Get minimum element - O(1)"""
        return self.items[0] if self.items else None
    
    def get_max(self):
        """Get maximum element - O(1)"""
        return self.items[-1] if self.items else None
    
    # Set operations
    def union(self, other_set):
        """Return union of two sets - O(n + m)"""
        result = OrderedSet()
        i, j = 0, 0
        
        while i < len(self.items) and j < len(other_set.items):
            if self.items[i] < other_set.items[j]:
                result.items.append(self.items[i])
                i += 1
            elif self.items[i] > other_set.items[j]:
                result.items.append(other_set.items[j])
                j += 1
            else:
                result.items.append(self.items[i])
                i += 1
                j += 1
        
        result.items.extend(self.items[i:])
        result.items.extend(other_set.items[j:])
        
        return result
    
    def intersection(self, other_set):
        """Return intersection of two sets - O(n + m)"""
        result = OrderedSet()
        i, j = 0, 0
        
        while i < len(self.items) and j < len(other_set.items):
            if self.items[i] < other_set.items[j]:
                i += 1
            elif self.items[i] > other_set.items[j]:
                j += 1
            else:
                result.items.append(self.items[i])
                i += 1
                j += 1
        
        return result
    
    def __str__(self):
        return f"{{{', '.join(map(str, self.items))}}}"


# Example usage and testing
if __name__ == "__main__":
    print("=== Unordered Set Demo ===\n")
    
    # Unordered Set
    uset = UnorderedSet()
    
    print("1. Adding elements:")
    for item in [5, 2, 8, 2, 9, 1, 5]:
        uset.add(item)
    print(f"Set after adding [5, 2, 8, 2, 9, 1, 5]: {uset}")
    
    print("\n2. Set operations:")
    print(f"Contains 5: {uset.contains(5)}")
    print(f"Contains 10: {uset.contains(10)}")
    print(f"Size: {uset.size()}")
    
    print("\n3. Removing elements:")
    uset.remove(2)
    print(f"After removing 2: {uset}")
    
    print("\n4. Set algebra:")
    uset2 = UnorderedSet()
    for item in [8, 9, 10, 11]:
        uset2.add(item)
    print(f"Set 1: {uset}")
    print(f"Set 2: {uset2}")
    print(f"Union: {uset.union(uset2)}")
    print(f"Intersection: {uset.intersection(uset2)}")
    print(f"Difference (1-2): {uset.difference(uset2)}")
    
    print("\n\n=== Ordered Set Demo ===\n")
    
    # Ordered Set
    oset = OrderedSet()
    
    print("1. Adding elements:")
    for item in [5, 2, 8, 2, 9, 1, 5]:
        oset.add(item)
    print(f"Set after adding [5, 2, 8, 2, 9, 1, 5]: {oset}")
    
    print("\n2. Set operations:")
    print(f"Contains 5: {oset.contains(5)}")
    print(f"Min element: {oset.get_min()}")
    print(f"Max element: {oset.get_max()}")
    
    print("\n3. Set algebra:")
    oset2 = OrderedSet()
    for item in [8, 9, 10, 11]:
        oset2.add(item)
    print(f"Set 1: {oset}")
    print(f"Set 2: {oset2}")
    print(f"Union: {oset.union(oset2)}")
    print(f"Intersection: {oset.intersection(oset2)}")
