/*
 * Doubly Linked List Implementation in C
 * Time Complexity:
 * - Insertion: O(1) at head/tail, O(n) at position
 * - Deletion: O(n)
 * - Traversal: O(n)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Node structure
typedef struct DNode {
    int data;
    struct DNode* prev;
    struct DNode* next;
} DNode;

// List structure to track head and tail
typedef struct DoublyLinkedList {
    DNode* head;
    DNode* tail;
} DoublyLinkedList;

// Create a new node
DNode* create_node(int data) {
    DNode* new_node = (DNode*)malloc(sizeof(DNode));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;
    return new_node;
}

// Initialize list
DoublyLinkedList* create_list() {
    DoublyLinkedList* list = (DoublyLinkedList*)malloc(sizeof(DoublyLinkedList));
    list->head = NULL;
    list->tail = NULL;
    return list;
}

// Insert at beginning - O(1)
void insert_at_beginning(DoublyLinkedList* list, int data) {
    DNode* new_node = create_node(data);
    
    if (list->head == NULL) {
        list->head = list->tail = new_node;
        return;
    }
    
    new_node->next = list->head;
    list->head->prev = new_node;
    list->head = new_node;
}

// Insert at end - O(1)
void insert_at_end(DoublyLinkedList* list, int data) {
    DNode* new_node = create_node(data);
    
    if (list->tail == NULL) {
        list->head = list->tail = new_node;
        return;
    }
    
    new_node->prev = list->tail;
    list->tail->next = new_node;
    list->tail = new_node;
}

// Insert at position - O(n)
void insert_at_position(DoublyLinkedList* list, int data, int position) {
    if (position == 0) {
        insert_at_beginning(list, data);
        return;
    }
    
    DNode* new_node = create_node(data);
    DNode* current = list->head;
    
    for (int i = 0; i < position - 1 && current != NULL; i++) {
        current = current->next;
    }
    
    if (current == NULL) {
        printf("Position out of bounds\n");
        free(new_node);
        return;
    }
    
    new_node->next = current->next;
    new_node->prev = current;
    
    if (current->next != NULL) {
        current->next->prev = new_node;
    } else {
        list->tail = new_node;
    }
    
    current->next = new_node;
}

// Delete by value - O(n)
void delete_by_value(DoublyLinkedList* list, int key) {
    if (list->head == NULL) {
        return;
    }
    
    DNode* current = list->head;
    
    while (current != NULL) {
        if (current->data == key) {
            // Delete head
            if (current == list->head) {
                list->head = current->next;
                if (list->head != NULL) {
                    list->head->prev = NULL;
                } else {
                    list->tail = NULL;
                }
            }
            // Delete tail
            else if (current == list->tail) {
                list->tail = current->prev;
                list->tail->next = NULL;
            }
            // Delete middle node
            else {
                current->prev->next = current->next;
                current->next->prev = current->prev;
            }
            
            free(current);
            return;
        }
        current = current->next;
    }
}

// Delete at position - O(n)
void delete_at_position(DoublyLinkedList* list, int position) {
    if (list->head == NULL) {
        return;
    }
    
    DNode* current = list->head;
    
    for (int i = 0; i < position && current != NULL; i++) {
        current = current->next;
    }
    
    if (current == NULL) {
        printf("Position out of bounds\n");
        return;
    }
    
    // Delete head
    if (current == list->head) {
        list->head = current->next;
        if (list->head != NULL) {
            list->head->prev = NULL;
        } else {
            list->tail = NULL;
        }
    }
    // Delete tail
    else if (current == list->tail) {
        list->tail = current->prev;
        list->tail->next = NULL;
    }
    // Delete middle node
    else {
        current->prev->next = current->next;
        current->next->prev = current->prev;
    }
    
    free(current);
}

// Display forward - O(n)
void display_forward(DoublyLinkedList* list) {
    DNode* current = list->head;
    
    printf("NULL <-> ");
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Display backward - O(n)
void display_backward(DoublyLinkedList* list) {
    DNode* current = list->tail;
    
    printf("NULL <-> ");
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->prev;
    }
    printf("NULL\n");
}

// Search - O(n)
int search(DoublyLinkedList* list, int key) {
    DNode* current = list->head;
    int position = 0;
    
    while (current != NULL) {
        if (current->data == key) {
            return position;
        }
        current = current->next;
        position++;
    }
    
    return -1;
}

// Get length - O(n)
int get_length(DoublyLinkedList* list) {
    int count = 0;
    DNode* current = list->head;
    
    while (current != NULL) {
        count++;
        current = current->next;
    }
    
    return count;
}

// Free all nodes - O(n)
void free_list(DoublyLinkedList* list) {
    DNode* current = list->head;
    DNode* next;
    
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    
    free(list);
}

// Main function for testing
int main() {
    printf("=== Doubly Linked List Demo (C) ===\n\n");
    
    DoublyLinkedList* list = create_list();
    
    // Insertion operations
    printf("1. Insertion Operations:\n");
    insert_at_beginning(list, 3);
    insert_at_beginning(list, 2);
    insert_at_beginning(list, 1);
    printf("After inserting 1, 2, 3 at beginning: ");
    display_forward(list);
    
    insert_at_end(list, 4);
    insert_at_end(list, 5);
    printf("After inserting 4, 5 at end: ");
    display_forward(list);
    
    insert_at_position(list, 10, 3);
    printf("After inserting 10 at position 3: ");
    display_forward(list);
    
    // Deletion operations
    printf("\n2. Deletion Operations:\n");
    delete_by_value(list, 10);
    printf("After deleting value 10: ");
    display_forward(list);
    
    delete_at_position(list, 0);
    printf("After deleting at position 0: ");
    display_forward(list);
    
    // Traversal operations
    printf("\n3. Traversal Operations:\n");
    printf("Forward: ");
    display_forward(list);
    printf("Backward: ");
    display_backward(list);
    
    // Other operations
    printf("\n4. Other Operations:\n");
    printf("Search for 3: Found at position %d\n", search(list, 3));
    printf("Length of list: %d\n", get_length(list));
    
    // Clean up
    free_list(list);
    
    return 0;
}
