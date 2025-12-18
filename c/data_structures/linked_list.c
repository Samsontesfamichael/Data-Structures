/*
 * Singly Linked List Implementation in C
 * Time Complexity:
 * - Insertion: O(1) at head, O(n) at tail
 * - Searching: O(n)
 * - Deletion: O(n)
 * - Traversal: O(n)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Create a new node
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (new_node == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

// Insert at beginning - O(1)
Node* insert_at_beginning(Node* head, int data) {
    Node* new_node = create_node(data);
    new_node->next = head;
    return new_node;
}

// Insert at end - O(n)
Node* insert_at_end(Node* head, int data) {
    Node* new_node = create_node(data);
    
    if (head == NULL) {
        return new_node;
    }
    
    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = new_node;
    
    return head;
}

// Insert at position - O(n)
Node* insert_at_position(Node* head, int data, int position) {
    if (position == 0) {
        return insert_at_beginning(head, data);
    }
    
    Node* new_node = create_node(data);
    Node* current = head;
    
    for (int i = 0; i < position - 1 && current != NULL; i++) {
        current = current->next;
    }
    
    if (current == NULL) {
        printf("Position out of bounds\n");
        free(new_node);
        return head;
    }
    
    new_node->next = current->next;
    current->next = new_node;
    
    return head;
}

// Search for a value - O(n)
int search(Node* head, int key) {
    Node* current = head;
    int position = 0;
    
    while (current != NULL) {
        if (current->data == key) {
            return position;
        }
        current = current->next;
        position++;
    }
    
    return -1; // Not found
}

// Delete by value - O(n)
Node* delete_by_value(Node* head, int key) {
    if (head == NULL) {
        return NULL;
    }
    
    // If head needs to be deleted
    if (head->data == key) {
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    Node* current = head;
    while (current->next != NULL) {
        if (current->next->data == key) {
            Node* temp = current->next;
            current->next = current->next->next;
            free(temp);
            return head;
        }
        current = current->next;
    }
    
    return head;
}

// Delete at position - O(n)
Node* delete_at_position(Node* head, int position) {
    if (head == NULL) {
        return NULL;
    }
    
    if (position == 0) {
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    Node* current = head;
    for (int i = 0; i < position - 1 && current->next != NULL; i++) {
        current = current->next;
    }
    
    if (current->next == NULL) {
        printf("Position out of bounds\n");
        return head;
    }
    
    Node* temp = current->next;
    current->next = current->next->next;
    free(temp);
    
    return head;
}

// Traverse and display - O(n)
void display(Node* head) {
    Node* current = head;
    
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Reverse the list - O(n)
Node* reverse(Node* head) {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    return prev;
}

// Get length - O(n)
int get_length(Node* head) {
    int count = 0;
    Node* current = head;
    
    while (current != NULL) {
        count++;
        current = current->next;
    }
    
    return count;
}

// Free all nodes - O(n)
void free_list(Node* head) {
    Node* current = head;
    Node* next;
    
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
}

// Main function for testing
int main() {
    printf("=== Singly Linked List Demo (C) ===\n\n");
    
    Node* head = NULL;
    
    // Insertion operations
    printf("1. Insertion Operations:\n");
    head = insert_at_beginning(head, 3);
    head = insert_at_beginning(head, 2);
    head = insert_at_beginning(head, 1);
    printf("After inserting 1, 2, 3 at beginning: ");
    display(head);
    
    head = insert_at_end(head, 4);
    head = insert_at_end(head, 5);
    printf("After inserting 4, 5 at end: ");
    display(head);
    
    head = insert_at_position(head, 10, 2);
    printf("After inserting 10 at position 2: ");
    display(head);
    
    // Searching operations
    printf("\n2. Searching Operations:\n");
    printf("Search for 3: Found at position %d\n", search(head, 3));
    printf("Search for 100: Found at position %d\n", search(head, 100));
    
    // Deletion operations
    printf("\n3. Deletion Operations:\n");
    head = delete_by_value(head, 10);
    printf("After deleting value 10: ");
    display(head);
    
    head = delete_at_position(head, 0);
    printf("After deleting at position 0: ");
    display(head);
    
    // Other operations
    printf("\n4. Other Operations:\n");
    printf("Length of list: %d\n", get_length(head));
    
    printf("\n5. Reversing the list:\n");
    head = reverse(head);
    printf("After reversing: ");
    display(head);
    
    // Clean up
    free_list(head);
    
    return 0;
}
