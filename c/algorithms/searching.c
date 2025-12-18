/*
 * Searching Algorithms Implementation in C
 * Includes: Sequential search, binary search, jump search, etc.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

// 10.1 Sequential Search (Linear Search)
int sequential_search(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

void sequential_search_all(int arr[], int n, int target, int* indices, int* count) {
    *count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            indices[(*count)++] = i;
        }
    }
}

// 10.2 Probability Search - Move to Front
int probability_search_mtf(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            // Move to front
            int temp = arr[i];
            for (int j = i; j > 0; j--) {
                arr[j] = arr[j - 1];
            }
            arr[0] = temp;
            return i; // Original position
        }
    }
    return -1;
}

// Probability Search - Transpose
int probability_search_transpose(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            if (i > 0) {
                // Swap with previous
                int temp = arr[i];
                arr[i] = arr[i - 1];
                arr[i - 1] = temp;
            }
            return i;
        }
    }
    return -1;
}

// Binary Search (Iterative)
int binary_search(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

// Binary Search (Recursive)
int binary_search_recursive_helper(int arr[], int target, int left, int right) {
    if (left > right) return -1;
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binary_search_recursive_helper(arr, target, mid + 1, right);
    } else {
        return binary_search_recursive_helper(arr, target, left, mid - 1);
    }
}

int binary_search_recursive(int arr[], int n, int target) {
    return binary_search_recursive_helper(arr, target, 0, n - 1);
}

// Binary Search - First Occurrence
int binary_search_first(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1; // Continue searching left
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

// Binary Search - Last Occurrence
int binary_search_last(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            left = mid + 1; // Continue searching right
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

// Jump Search
int jump_search(int arr[], int n, int target) {
    int step = sqrt(n);
    int prev = 0;
    
    // Find block where element may be present
    while (arr[(step < n ? step : n) - 1] < target) {
        prev = step;
        step += sqrt(n);
        if (prev >= n) return -1;
    }
    
    // Linear search in block
    while (arr[prev] < target) {
        prev++;
        if (prev == (step < n ? step : n)) return -1;
    }
    
    if (arr[prev] == target) return prev;
    
    return -1;
}

// Interpolation Search
int interpolation_search(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        if (left == right) {
            if (arr[left] == target) return left;
            return -1;
        }
        
        // Interpolation formula
        int pos = left + (((double)(target - arr[left]) / 
                         (arr[right] - arr[left])) * (right - left));
        
        if (arr[pos] == target) {
            return pos;
        } else if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
        }
    }
    
    return -1;
}

// Utility function to print array
void print_array(int arr[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i < n - 1) printf(", ");
    }
    printf("]");
}

// Main function for testing
int main() {
    printf("=== Searching Algorithms Demo (C) ===\n\n");
    
    // Sequential Search
    printf("1. Sequential Search:\n");
    int arr[] = {64, 34, 25, 12, 22, 11, 90, 22};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("  Array: ");
    print_array(arr, n);
    printf("\n");
    printf("  Search for 22: Found at index %d\n", sequential_search(arr, n, 22));
    printf("  Search for 100: Found at index %d\n", sequential_search(arr, n, 100));
    
    int indices[100];
    int count;
    sequential_search_all(arr, n, 22, indices, &count);
    printf("  All occurrences of 22: [");
    for (int i = 0; i < count; i++) {
        printf("%d", indices[i]);
        if (i < count - 1) printf(", ");
    }
    printf("]\n");
    
    // Probability Search
    printf("\n2. Probability Search (Move-to-Front):\n");
    int ps_arr[] = {10, 20, 30, 40, 50};
    int ps_n = 5;
    printf("  Initial: ");
    print_array(ps_arr, ps_n);
    printf("\n");
    
    probability_search_mtf(ps_arr, ps_n, 40);
    printf("  After searching 40: ");
    print_array(ps_arr, ps_n);
    printf("\n");
    
    // Binary Search
    printf("\n3. Binary Search (on sorted array):\n");
    int sorted_arr[] = {11, 12, 22, 25, 34, 64, 90};
    int sorted_n = sizeof(sorted_arr) / sizeof(sorted_arr[0]);
    printf("  Sorted array: ");
    print_array(sorted_arr, sorted_n);
    printf("\n");
    printf("  Search for 25: Found at index %d\n", binary_search(sorted_arr, sorted_n, 25));
    printf("  Search for 100: Found at index %d\n", binary_search(sorted_arr, sorted_n, 100));
    
    // Binary Search with duplicates
    printf("\n4. Binary Search (with duplicates):\n");
    int dup_arr[] = {1, 2, 2, 2, 3, 4, 5, 5, 5, 6};
    int dup_n = sizeof(dup_arr) / sizeof(dup_arr[0]);
    printf("  Array: ");
    print_array(dup_arr, dup_n);
    printf("\n");
    printf("  First occurrence of 2: index %d\n", binary_search_first(dup_arr, dup_n, 2));
    printf("  Last occurrence of 2: index %d\n", binary_search_last(dup_arr, dup_n, 2));
    printf("  First occurrence of 5: index %d\n", binary_search_first(dup_arr, dup_n, 5));
    printf("  Last occurrence of 5: index %d\n", binary_search_last(dup_arr, dup_n, 5));
    
    // Jump Search
    printf("\n5. Jump Search:\n");
    printf("  Array: ");
    print_array(sorted_arr, sorted_n);
    printf("\n");
    printf("  Search for 64: Found at index %d\n", jump_search(sorted_arr, sorted_n, 64));
    
    // Interpolation Search
    printf("\n6. Interpolation Search:\n");
    int uniform_arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int uniform_n = sizeof(uniform_arr) / sizeof(uniform_arr[0]);
    printf("  Array: ");
    print_array(uniform_arr, uniform_n);
    printf("\n");
    printf("  Search for 70: Found at index %d\n", interpolation_search(uniform_arr, uniform_n, 70));
    
    return 0;
}
