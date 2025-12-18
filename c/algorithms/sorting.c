/*
 * Sorting Algorithms Implementation in C
 * Includes: Bubble, Merge, Quick, Insertion, Shell, and Radix Sort
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Utility function to swap two elements
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Print array
void print_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Check if array is sorted
int is_sorted(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return 0;
        }
    }
    return 1;
}

// ===== BUBBLE SORT =====
// Time: O(n²), Space: O(1)
void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = 1;
            }
        }
        if (!swapped) break;
    }
}

// ===== MERGE SORT =====
// Time: O(n log n), Space: O(n)
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int* L = (int*)malloc(n1 * sizeof(int));
    int* R = (int*)malloc(n2 * sizeof(int));
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    
    free(L);
    free(R);
}

void merge_sort_helper(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        merge_sort_helper(arr, left, mid);
        merge_sort_helper(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void merge_sort(int arr[], int n) {
    merge_sort_helper(arr, 0, n - 1);
}

// ===== QUICK SORT =====
// Time: O(n log n) average, O(n²) worst, Space: O(log n)
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quick_sort_helper(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        
        quick_sort_helper(arr, low, pi - 1);
        quick_sort_helper(arr, pi + 1, high);
    }
}

void quick_sort(int arr[], int n) {
    quick_sort_helper(arr, 0, n - 1);
}

// ===== INSERTION SORT =====
// Time: O(n²), Space: O(1)
void insertion_sort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = key;
    }
}

// ===== SHELL SORT =====
// Time: O(n log n) to O(n²), Space: O(1)
void shell_sort(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            
            arr[j] = temp;
        }
    }
}

// ===== RADIX SORT =====
// Time: O(d * (n + k)), Space: O(n + k)
int get_max(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

void counting_sort_by_digit(int arr[], int n, int exp) {
    int* output = (int*)malloc(n * sizeof(int));
    int count[10] = {0};
    
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }
    
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    free(output);
}

void radix_sort(int arr[], int n) {
    int max = get_max(arr, n);
    
    for (int exp = 1; max / exp > 0; exp *= 10) {
        counting_sort_by_digit(arr, n, exp);
    }
}

// Main function for testing
int main() {
    printf("=== Sorting Algorithms Demo (C) ===\n\n");
    
    int test_arr[] = {64, 34, 25, 12, 22, 11, 90, 88, 45, 50};
    int n = sizeof(test_arr) / sizeof(test_arr[0]);
    
    // Test each sorting algorithm
    printf("Original array: ");
    print_array(test_arr, n);
    printf("\n");
    
    // Bubble Sort
    int arr1[10];
    memcpy(arr1, test_arr, sizeof(test_arr));
    bubble_sort(arr1, n);
    printf("Bubble Sort:    ");
    print_array(arr1, n);
    printf("Sorted: %s\n\n", is_sorted(arr1, n) ? "Yes" : "No");
    
    // Merge Sort
    int arr2[10];
    memcpy(arr2, test_arr, sizeof(test_arr));
    merge_sort(arr2, n);
    printf("Merge Sort:     ");
    print_array(arr2, n);
    printf("Sorted: %s\n\n", is_sorted(arr2, n) ? "Yes" : "No");
    
    // Quick Sort
    int arr3[10];
    memcpy(arr3, test_arr, sizeof(test_arr));
    quick_sort(arr3, n);
    printf("Quick Sort:     ");
    print_array(arr3, n);
    printf("Sorted: %s\n\n", is_sorted(arr3, n) ? "Yes" : "No");
    
    // Insertion Sort
    int arr4[10];
    memcpy(arr4, test_arr, sizeof(test_arr));
    insertion_sort(arr4, n);
    printf("Insertion Sort: ");
    print_array(arr4, n);
    printf("Sorted: %s\n\n", is_sorted(arr4, n) ? "Yes" : "No");
    
    // Shell Sort
    int arr5[10];
    memcpy(arr5, test_arr, sizeof(test_arr));
    shell_sort(arr5, n);
    printf("Shell Sort:     ");
    print_array(arr5, n);
    printf("Sorted: %s\n\n", is_sorted(arr5, n) ? "Yes" : "No");
    
    // Radix Sort
    int arr6[10];
    memcpy(arr6, test_arr, sizeof(test_arr));
    radix_sort(arr6, n);
    printf("Radix Sort:     ");
    print_array(arr6, n);
    printf("Sorted: %s\n\n", is_sorted(arr6, n) ? "Yes" : "No");
    
    return 0;
}
