/*
 * Queue Implementations in C
 * - Standard Queue (FIFO)
 * - Circular Queue
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

// ===== STANDARD QUEUE =====
typedef struct Queue {
    int data[MAX_SIZE];
    int front;
    int rear;
    int size;
} Queue;

Queue* create_queue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = 0;
    q->rear = -1;
    q->size = 0;
    return q;
}

bool is_empty(Queue* q) {
    return q->size == 0;
}

bool is_full(Queue* q) {
    return q->size == MAX_SIZE;
}

void enqueue(Queue* q, int value) {
    if (is_full(q)) {
        printf("Queue is full\n");
        return;
    }
    
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = value;
    q->size++;
}

int dequeue(Queue* q) {
    if (is_empty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    
    int value = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->size--;
    
    return value;
}

int peek(Queue* q) {
    if (is_empty(q)) {
        printf("Queue is empty\n");
        return -1;
    }
    return q->data[q->front];
}

void display_queue(Queue* q) {
    if (is_empty(q)) {
        printf("Queue is empty\n");
        return;
    }
    
    printf("Queue: ");
    int index = q->front;
    for (int i = 0; i < q->size; i++) {
        printf("%d ", q->data[index]);
        index = (index + 1) % MAX_SIZE;
    }
    printf("\n");
}

// ===== DEQUE (Double Ended Queue) =====
typedef struct Deque {
    int data[MAX_SIZE];
    int front;
    int rear;
    int size;
} Deque;

Deque* create_deque() {
    Deque* dq = (Deque*)malloc(sizeof(Deque));
    dq->front = -1;
    dq->rear = 0;
    dq->size = 0;
    return dq;
}

bool deque_is_empty(Deque* dq) {
    return dq->size == 0;
}

bool deque_is_full(Deque* dq) {
    return dq->size == MAX_SIZE;
}

void add_front(Deque* dq, int value) {
    if (deque_is_full(dq)) {
        printf("Deque is full\n");
        return;
    }
    
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else {
        dq->front = (dq->front - 1 + MAX_SIZE) % MAX_SIZE;
    }
    
    dq->data[dq->front] = value;
    dq->size++;
}

void add_rear(Deque* dq, int value) {
    if (deque_is_full(dq)) {
        printf("Deque is full\n");
        return;
    }
    
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else {
        dq->rear = (dq->rear + 1) % MAX_SIZE;
    }
    
    dq->data[dq->rear] = value;
    dq->size++;
}

int remove_front(Deque* dq) {
    if (deque_is_empty(dq)) {
        printf("Deque is empty\n");
        return -1;
    }
    
    int value = dq->data[dq->front];
    
    if (dq->size == 1) {
        dq->front = -1;
        dq->rear = 0;
    } else {
        dq->front = (dq->front + 1) % MAX_SIZE;
    }
    
    dq->size--;
    return value;
}

int remove_rear(Deque* dq) {
    if (deque_is_empty(dq)) {
        printf("Deque is empty\n");
        return -1;
    }
    
    int value = dq->data[dq->rear];
    
    if (dq->size == 1) {
        dq->front = -1;
        dq->rear = 0;
    } else {
        dq->rear = (dq->rear - 1 + MAX_SIZE) % MAX_SIZE;
    }
    
    dq->size--;
    return value;
}

void display_deque(Deque* dq) {
    if (deque_is_empty(dq)) {
        printf("Deque is empty\n");
        return;
    }
    
    printf("Deque: ");
    int index = dq->front;
    for (int i = 0; i < dq->size; i++) {
        printf("%d ", dq->data[index]);
        index = (index + 1) % MAX_SIZE;
    }
    printf("\n");
}

// Main function for testing
int main() {
    printf("=== Queue Implementations Demo (C) ===\n\n");
    
    // Standard Queue
    printf("1. Standard Queue:\n");
    Queue* q = create_queue();
    
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);
    enqueue(q, 40);
    display_queue(q);
    
    printf("Dequeued: %d\n", dequeue(q));
    printf("Front element: %d\n", peek(q));
    display_queue(q);
    
    // Deque
    printf("\n2. Double Ended Queue (Deque):\n");
    Deque* dq = create_deque();
    
    add_rear(dq, 3);
    add_rear(dq, 4);
    add_front(dq, 2);
    add_front(dq, 1);
    add_rear(dq, 5);
    display_deque(dq);
    
    printf("Remove from front: %d\n", remove_front(dq));
    printf("Remove from rear: %d\n", remove_rear(dq));
    display_deque(dq);
    
    // Clean up
    free(q);
    free(dq);
    
    return 0;
}
