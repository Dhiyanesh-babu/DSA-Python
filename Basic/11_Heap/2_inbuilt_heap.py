import heapq

# 1. Creating a Heap
data = [5, 7, 9, 1, 3]
heapq.heapify(data)  # Transforms list into a heap
print("Heap:", data)  # Output: Heap: [1, 3, 9, 7, 5]

# 2. Pushing an Element
heapq.heappush(data, 2)  # Adds 2 to the heap
print("After heappush:", data)  # Output: After heappush: [1, 2, 9, 7, 5, 3]

# 3. Popping the Smallest Element
smallest = heapq.heappop(data)  # Removes and returns the smallest element
print("Popped element:", smallest)  # Output: Popped element: 1
print("After heappop:", data)  # Output: After heappop: [2, 3, 9, 7, 5]

# 4. Replacing the Smallest Element
replaced = heapq.heappushpop(data, 4)  # Pops the smallest and pushes 4
print("Replaced element:", replaced)  # Output: Replaced element: 2
print("After heappushpop:", data)  # Output: After heappushpop: [3, 4, 9, 7, 5]

# 5. Heapify
another_data = [10, 20, 15]
heapq.heapify(another_data)  # Converts list into a heap
print("Heapified another_data:", another_data)  # Output: Heapified another_data: [10, 20, 15]

# 6. Finding the n Smallest Elements
n_smallest = heapq.nsmallest(3, data)  # Returns 3 smallest elements
print("Three smallest elements:", n_smallest)  # Output: Three smallest elements: [3, 4, 5]

# 7. Finding the n Largest Elements
n_largest = heapq.nlargest(3, data)  # Returns 3 largest elements
print("Three largest elements:", n_largest)  # Output: Three largest elements: [9, 7, 5]


print('\n\n\n')

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        # Invert the value by multiplying by -1
        heapq.heappush(self.heap, -item)

    def pop(self):
        # Invert the value back to positive before returning
        return -heapq.heappop(self.heap)

    def peek(self):
        # Return the largest element without removing it
        return -self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

# Example usage
max_heap = MaxHeap()
max_heap.push(5)
max_heap.push(2)
max_heap.push(8)
max_heap.push(1)

print("Max Heap after adding elements:", [-x for x in max_heap.heap])  # Output: [8, 5, 2, 1]

max_element = max_heap.pop()
print("Popped max element:", max_element)  # Output: Popped max element: 8
print("Max Heap after popping:", [-x for x in max_heap.heap])  # Output: [5, 2, 1]

print("Current max element (peek):", max_heap.peek())  # Output: Current max element (peek): 5
print("Size of max heap:", max_heap.size())  # Output: Size of max heap: 3
print("Is the max heap empty?", max_heap.is_empty())  # Output: Is the max heap empty? False









