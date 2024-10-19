# import queue

# # Create a queue
# q = queue.Queue()

# # Enqueue operation (Add element to the rear of the queue)
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(40)
# # Peek operation (Check the front element without removing it)
# # Since `queue.Queue` does not have a direct 'peek' method, we'll use `queue.queue` (which is the internal deque) to access it.
# if not q.empty():
#     print(f"Front element: {q.queue[0]}")  # Output: Front element: 10

# # Dequeue operation (Remove element from the front of the queue)
# print(q.get())  # Output: 10
# print(q.get())  # Output: 20

# # Check if the queue is empty
# if q.empty():
#     print("Queue is empty now.")
# else:
#     print(f"Next front element: {q.queue[0]}")  # Output: Next front element: 30

# # Dequeue the last element
# print(q.get())  # Output: 30


from collections import deque

class Queue:
    def __init__(self):
        # Initialize a deque to represent the queue
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return an item from the front of the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def peek(self):
        """Return the front item of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("peek from an empty queue")

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    print("Queue size:", q.size())  # Output: Queue size: 3
    print("Front item:", q.peek())   # Output: Front item: 1
    print("Dequeue:", q.dequeue())    # Output: Dequeue: 1
    print("Queue size after dequeue:", q.size())  # Output: Queue size after dequeue: 2
    print("Is queue empty?", q.is_empty())  # Output: Is queue empty? False

