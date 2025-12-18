"""
Sorting Algorithms Implementation
All major sorting algorithms with time and space complexity analysis
"""

def bubble_sort(arr):
    """
    Bubble Sort - O(n²) time, O(1) space
    Repeatedly steps through list, compares adjacent elements and swaps if wrong order
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps, array is sorted
        if not swapped:
            break
    
    return arr


def merge_sort(arr):
    """
    Merge Sort - O(n log n) time, O(n) space
    Divide and conquer algorithm that divides array into halves, sorts them and merges
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return _merge(left, right)


def _merge(left, right):
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr):
    """
    Quick Sort - O(n log n) average, O(n²) worst case time, O(log n) space
    Picks pivot element and partitions array around it
    """
    if len(arr) <= 1:
        return arr
    
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr, low, high):
    """Helper function for quick sort"""
    if low < high:
        # Partition and get pivot index
        pi = _partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def _partition(arr, low, high):
    """Partition function for quick sort"""
    # Choose rightmost element as pivot
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def insertion_sort(arr):
    """
    Insertion Sort - O(n²) time, O(1) space
    Builds final sorted array one item at a time
    Efficient for small data sets
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def shell_sort(arr):
    """
    Shell Sort - O(n log n) to O(n²) time depending on gap sequence, O(1) space
    Variation of insertion sort that allows exchange of far items
    """
    arr = arr.copy()
    n = len(arr)
    
    # Start with large gap, then reduce
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Shift earlier gap-sorted elements up until correct location found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    return arr


def radix_sort(arr):
    """
    Radix Sort - O(d * (n + k)) time, O(n + k) space
    where d is number of digits, k is range of digits (0-9)
    Non-comparison based sorting for integers
    """
    if not arr:
        return arr
    
    # Handle negative numbers by separating them
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]
    
    # Sort positives
    if positives:
        positives = _radix_sort_positive(positives)
    
    # Sort negatives (sort absolute values, then reverse)
    if negatives:
        negatives = [-x for x in negatives]
        negatives = _radix_sort_positive(negatives)
        negatives = [-x for x in reversed(negatives)]
    
    return negatives + positives


def _radix_sort_positive(arr):
    """Helper for radix sort on positive integers"""
    if not arr:
        return arr
    
    # Find maximum number to know number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def _counting_sort_by_digit(arr, exp):
    """Counting sort based on digit represented by exp"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Change count[i] so it contains actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    return output


def counting_sort(arr):
    """
    Counting Sort - O(n + k) time, O(k) space
    where k is range of input
    Works well when range is not significantly greater than n
    """
    if not arr:
        return arr
    
    # Find range
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    # Create count array
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] to contain actual position
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


# Utility functions for testing
def is_sorted(arr):
    """Check if array is sorted"""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def test_sorting_algorithm(sort_func, test_arrays):
    """Test a sorting algorithm with multiple test cases"""
    print(f"\nTesting {sort_func.__name__}:")
    print(f"Time Complexity: {sort_func.__doc__.split('-')[1].split('time')[0].strip()}")
    
    for arr in test_arrays:
        sorted_arr = sort_func(arr)
        status = "[OK]" if is_sorted(sorted_arr) else "[FAIL]"
        print(f"  {status} {arr[:10]}{'...' if len(arr) > 10 else ''} -> "
              f"{sorted_arr[:10]}{'...' if len(sorted_arr) > 10 else ''}")


# Example usage and testing
if __name__ == "__main__":
    print("=== Sorting Algorithms Demo ===\n")
    
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [-5, 2, -8, 1, 9, -3],
        list(range(10, 0, -1))  # Reverse sorted
    ]
    
    # Test all sorting algorithms
    algorithms = [
        bubble_sort,
        merge_sort,
        quick_sort,
        insertion_sort,
        shell_sort,
        radix_sort,
        counting_sort
    ]
    
    for algo in algorithms:
        test_sorting_algorithm(algo, test_arrays)
    
    # Performance comparison on larger array
    print("\n\n=== Performance Comparison ===")
    import time
    import random
    
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    print(f"\nSorting array of {len(large_array)} random elements:")
    
    for algo in algorithms:
        arr_copy = large_array.copy()
        start = time.time()
        result = algo(arr_copy)
        end = time.time()
        
        print(f"  {algo.__name__:20s}: {(end - start)*1000:.2f} ms "
              f"{'[OK]' if is_sorted(result) else '[FAIL]'}")
