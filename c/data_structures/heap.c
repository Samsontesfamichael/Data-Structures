/*
 * Min Heap Implementation in C
 * Time Complexity:
 * - Insertion: O(log n)
 * - Extract Min: O(log n)
 * - Get Min: O(1)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_HEAP_SIZE 100

typedef struct MinHeap {
    int data[MAX_HEAP_SIZE];
    int size;
} MinHeap;

// Initialize heap
MinHeap* create_heap() {
    MinHeap* heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->size = 0;
    return heap;
}

// Helper functions
int parent(int i) { return (i - 1) / 2; }
int left_child(int i) { return 2 * i + 1; }
int right_child(int i) { return 2 * i + 2; }

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Heapify up - O(log n)
void heapify_up(MinHeap* heap, int index) {
    while (index > 0 && heap->data[parent(index)] > heap->data[index]) {
        swap(&heap->data[index], &heap->data[parent(index)]);
        index = parent(index);
    }
}

// Heapify down - O(log n)
void heapify_down(MinHeap* heap, int index) {
    int smallest = index;
    int left = left_child(index);
    int right = right_child(index);
    
    if (left < heap->size && heap->data[left] < heap->data[smallest]) {
        smallest = left;
    }
    
    if (right < heap->size && heap->data[right] < heap->data[smallest]) {
        smallest = right;
    }
    
    if (smallest != index) {
        swap(&heap->data[index], &heap->data[smallest]);
        heapify_down(heap, smallest);
    }
}

// Insert element - O(log n)
void insert(MinHeap* heap, int value) {
    if (heap->size >= MAX_HEAP_SIZE) {
        printf("Heap is full\n");
        return;
    }
    
    heap->data[heap->size] = value;
    heapify_up(heap, heap->size);
    heap->size++;
}

// Extract minimum - O(log n)
int extract_min(MinHeap* heap) {
    if (heap->size == 0) {
        printf("Heap is empty\n");
        return -1;
    }
    
    int min = heap->data[0];
    heap->data[0] = heap->data[heap->size - 1];
    heap->size--;
    heapify_down(heap, 0);
    
    return min;
}

// Get minimum - O(1)
int get_min(MinHeap* heap) {
    if (heap->size == 0) {
        printf("Heap is empty\n");
        return -1;
    }
    return heap->data[0];
}

// Display heap
void display(MinHeap* heap) {
    printf("Heap: ");
    for (int i = 0; i < heap->size; i++) {
        printf("%d ", heap->data[i]);
    }
    printf("\n");
}

// Main function for testing
int main() {
    printf("=== Min Heap Demo (C) ===\n\n");
    
    MinHeap* heap = create_heap();
    
    // Insertion
    printf("1. Insertion Operations:\n");
    int values[] = {50, 30, 20, 15, 10, 8, 16};
    for (int i = 0; i < 7; i++) {
        insert(heap, values[i]);
    }
    printf("After inserting: ");
    display(heap);
    printf("Min element: %d\n", get_min(heap));
    
    // Extract min
    printf("\n2. Extract Min Operations:\n");
    printf("Extracted: %d\n", extract_min(heap));
    printf("Extracted: %d\n", extract_min(heap));
    printf("After extractions: ");
    display(heap);
    printf("New min: %d\n", get_min(heap));
    
    // Clean up
    free(heap);
    
    return 0;
}
