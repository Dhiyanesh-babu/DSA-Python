import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        # The heapq library implements a min-heap, so we use a tuple (priority, item)
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        # Pop the element with the highest priority (lowest number)
        return heapq.heappop(self.elements)[1]

    def peek(self):
        # Peek at the element with the highest priority
        return self.elements[0][1] if self.elements else None

# Example usage
pq = PriorityQueue()
pq.put("task1", priority=3)
pq.put("task2", priority=1)
pq.put("task3", priority=2)

while not pq.is_empty():
    print(pq.get())
