"""
Searching Algorithms Implementation
Includes: Sequential search, probability search, binary search
"""

# 10.1 Sequential Search (Linear Search)
def sequential_search(arr, target):
    """
    Linear search through array - O(n) time, O(1) space
    Returns index if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def sequential_search_all(arr, target):
    """
    Find all occurrences of target - O(n) time
    Returns list of indices
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


# 10.2 Probability Search (Self-Organizing Search)
class ProbabilitySearch:
    """
    Self-organizing search that moves frequently accessed items to front
    Improves performance for non-uniform access patterns
    """
    
    def __init__(self, items):
        self.items = list(items)
    
    def search_move_to_front(self, target):
        """
        Move-to-front heuristic - O(n) time
        Moves found item to beginning of list
        """
        for i in range(len(self.items)):
            if self.items[i] == target:
                # Move to front
                item = self.items.pop(i)
                self.items.insert(0, item)
                return i  # Original position
        return -1
    
    def search_transpose(self, target):
        """
        Transpose heuristic - O(n) time
        Swaps found item with predecessor
        """
        for i in range(len(self.items)):
            if self.items[i] == target:
                if i > 0:
                    # Swap with previous item
                    self.items[i], self.items[i-1] = self.items[i-1], self.items[i]
                return i
        return -1
    
    def search_count(self, target, counts):
        """
        Frequency count heuristic - O(n) time
        Maintains items sorted by access frequency
        """
        for i in range(len(self.items)):
            if self.items[i] == target:
                counts[target] = counts.get(target, 0) + 1
                
                # Bubble up based on count
                j = i
                while j > 0 and counts.get(self.items[j], 0) > counts.get(self.items[j-1], 0):
                    self.items[j], self.items[j-1] = self.items[j-1], self.items[j]
                    j -= 1
                
                return i
        return -1
    
    def get_items(self):
        return self.items.copy()


# Binary Search (bonus - efficient for sorted arrays)
def binary_search(arr, target):
    """
    Binary search on sorted array - O(log n) time, O(1) space
    Returns index if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search - O(log n) time, O(log n) space
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array with duplicates
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_last_occurrence(arr, target):
    """
    Find last occurrence of target in sorted array with duplicates
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Jump Search (bonus)
def jump_search(arr, target):
    """
    Jump search for sorted array - O(√n) time
    """
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    
    # Find block where element may be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    
    # Linear search in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


# Interpolation Search (bonus)
def interpolation_search(arr, target):
    """
    Interpolation search for uniformly distributed sorted array
    O(log log n) average, O(n) worst
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Interpolation formula
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


# Example usage and testing
if __name__ == "__main__":
    print("=== Searching Algorithms Demo ===\n")
    
    # Sequential Search
    print("1. Sequential Search:")
    arr = [64, 34, 25, 12, 22, 11, 90, 22]
    print(f"  Array: {arr}")
    print(f"  Search for 22: Found at index {sequential_search(arr, 22)}")
    print(f"  Search for 100: Found at index {sequential_search(arr, 100)}")
    print(f"  All occurrences of 22: {sequential_search_all(arr, 22)}")
    
    # Probability Search
    print("\n2. Probability Search (Move-to-Front):")
    ps = ProbabilitySearch([10, 20, 30, 40, 50])
    print(f"  Initial: {ps.get_items()}")
    ps.search_move_to_front(40)
    print(f"  After searching 40: {ps.get_items()}")
    ps.search_move_to_front(20)
    print(f"  After searching 20: {ps.get_items()}")
    
    print("\n3. Probability Search (Transpose):")
    ps2 = ProbabilitySearch([10, 20, 30, 40, 50])
    print(f"  Initial: {ps2.get_items()}")
    ps2.search_transpose(40)
    print(f"  After searching 40: {ps2.get_items()}")
    ps2.search_transpose(40)
    print(f"  After searching 40 again: {ps2.get_items()}")
    
    # Binary Search
    print("\n4. Binary Search (on sorted array):")
    sorted_arr = [11, 12, 22, 25, 34, 64, 90]
    print(f"  Sorted array: {sorted_arr}")
    print(f"  Search for 25: Found at index {binary_search(sorted_arr, 25)}")
    print(f"  Search for 100: Found at index {binary_search(sorted_arr, 100)}")
    
    # Binary Search with duplicates
    print("\n5. Binary Search (with duplicates):")
    dup_arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    print(f"  Array: {dup_arr}")
    print(f"  First occurrence of 2: index {binary_search_first_occurrence(dup_arr, 2)}")
    print(f"  Last occurrence of 2: index {binary_search_last_occurrence(dup_arr, 2)}")
    print(f"  First occurrence of 5: index {binary_search_first_occurrence(dup_arr, 5)}")
    print(f"  Last occurrence of 5: index {binary_search_last_occurrence(dup_arr, 5)}")
    
    # Jump Search
    print("\n6. Jump Search:")
    print(f"  Array: {sorted_arr}")
    print(f"  Search for 64: Found at index {jump_search(sorted_arr, 64)}")
    
    # Interpolation Search
    print("\n7. Interpolation Search:")
    uniform_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"  Array: {uniform_arr}")
    print(f"  Search for 70: Found at index {interpolation_search(uniform_arr, 70)}")
    
    # Performance comparison
    print("\n8. Performance Comparison:")
    import time
    large_arr = list(range(0, 10000, 2))  # Even numbers 0-9998
    target = 5000
    
    start = time.time()
    sequential_search(large_arr, target)
    seq_time = (time.time() - start) * 1000
    
    start = time.time()
    binary_search(large_arr, target)
    bin_time = (time.time() - start) * 1000
    
    print(f"  Array size: {len(large_arr)}")
    print(f"  Sequential search: {seq_time:.4f} ms")
    print(f"  Binary search: {bin_time:.4f} ms")
    print(f"  Binary is {seq_time/bin_time:.1f}x faster" if bin_time > 0 else "")
