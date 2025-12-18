"""
Queue Implementations
- Standard Queue (FIFO)
- Priority Queue
- Double Ended Queue (Deque)

Time Complexity varies by implementation
"""

from collections import deque as collections_deque
import heapq

class Queue:
    """Standard FIFO Queue implementation"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return item from front - O(n) due to list shift"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Get front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def rear(self):
        """Get rear item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Get size of queue - O(1)"""
        return len(self.items)
    
    def clear(self):
        """Clear all items - O(1)"""
        self.items.clear()
    
    def __str__(self):
        return f"Front -> {self.items} <- Rear"


class PriorityQueue:
    """Priority Queue implementation using min heap"""
    
    def __init__(self):
        self.heap = []
        self.counter = 0  # For stable sorting
    
    def enqueue(self, item, priority):
        """Add item with priority - O(log n)
        Lower priority value = higher priority
        """
        # Use counter to maintain insertion order for same priorities
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1
    
    def dequeue(self):
        """Remove and return highest priority item - O(log n)"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        priority, _, item = heapq.heappop(self.heap)
        return item, priority
    
    def peek(self):
        """Get highest priority item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        priority, _, item = self.heap[0]
        return item, priority
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self.heap) == 0
    
    def size(self):
        """Get size of queue - O(1)"""
        return len(self.heap)
    
    def clear(self):
        """Clear all items - O(1)"""
        self.heap.clear()
        self.counter = 0
    
    def __str__(self):
        items = [(item, priority) for priority, _, item in sorted(self.heap)]
        return f"PriorityQueue: {items}"


class Deque:
    """Double Ended Queue implementation"""
    
    def __init__(self):
        self.items = collections_deque()
    
    # Add operations
    def add_front(self, item):
        """Add item to front - O(1)"""
        self.items.appendleft(item)
    
    def add_rear(self, item):
        """Add item to rear - O(1)"""
        self.items.append(item)
    
    # Remove operations
    def remove_front(self):
        """Remove and return item from front - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.popleft()
    
    def remove_rear(self):
        """Remove and return item from rear - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()
    
    # Peek operations
    def peek_front(self):
        """Get front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]
    
    def peek_rear(self):
        """Get rear item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if deque is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Get size of deque - O(1)"""
        return len(self.items)
    
    def clear(self):
        """Clear all items - O(1)"""
        self.items.clear()
    
    def __str__(self):
        return f"Front <- {list(self.items)} -> Rear"


# Example usage and testing
if __name__ == "__main__":
    print("=== Standard Queue Demo ===\n")
    
    q = Queue()
    
    print("1. Enqueue operations:")
    for item in [1, 2, 3, 4, 5]:
        q.enqueue(item)
    print(f"After enqueuing 1-5: {q}")
    
    print("\n2. Dequeue operations:")
    print(f"Dequeued: {q.dequeue()}")
    print(f"Dequeued: {q.dequeue()}")
    print(f"After dequeuing twice: {q}")
    
    print("\n3. Peek operations:")
    print(f"Front: {q.front()}")
    print(f"Rear: {q.rear()}")
    print(f"Size: {q.size()}")
    
    print("\n\n=== Priority Queue Demo ===\n")
    
    pq = PriorityQueue()
    
    print("1. Enqueue with priorities:")
    pq.enqueue("Low priority task", 5)
    pq.enqueue("High priority task", 1)
    pq.enqueue("Medium priority task", 3)
    pq.enqueue("Critical task", 0)
    pq.enqueue("Another medium task", 3)
    print(pq)
    
    print("\n2. Dequeue by priority:")
    while not pq.is_empty():
        item, priority = pq.dequeue()
        print(f"  Dequeued: '{item}' (priority: {priority})")
    
    print("\n\n=== Double Ended Queue (Deque) Demo ===\n")
    
    dq = Deque()
    
    print("1. Add operations:")
    dq.add_rear(3)
    dq.add_rear(4)
    dq.add_front(2)
    dq.add_front(1)
    dq.add_rear(5)
    print(f"After mixed additions: {dq}")
    
    print("\n2. Remove operations:")
    print(f"Remove from front: {dq.remove_front()}")
    print(f"Remove from rear: {dq.remove_rear()}")
    print(f"After removals: {dq}")
    
    print("\n3. Peek operations:")
    print(f"Peek front: {dq.peek_front()}")
    print(f"Peek rear: {dq.peek_rear()}")
    
    print("\n4. Using deque as stack (LIFO):")
    stack = Deque()
    stack.add_rear(1)
    stack.add_rear(2)
    stack.add_rear(3)
    print(f"Stack: {stack}")
    print(f"Pop: {stack.remove_rear()}")
    print(f"Pop: {stack.remove_rear()}")
    
    print("\n5. Using deque as queue (FIFO):")
    queue = Deque()
    queue.add_rear(1)
    queue.add_rear(2)
    queue.add_rear(3)
    print(f"Queue: {queue}")
    print(f"Dequeue: {queue.remove_front()}")
    print(f"Dequeue: {queue.remove_front()}")
