class heap:
    def __init__(self,c) -> None:
        self.capacity = c
        self.size = 0
        self.arr = [0]*c
    
    def left(self,i):
        return 2*i + 1
    def right(self,i):
        return 2*i + 2
    def parent(self,i):
        return (i-1)//2
    def show(self):
        print(self.arr[:self.size])
    def insert(self,x):
        if self.size == self.capacity:
            return
        self.size += 1
        self.arr[self.size-1] = x
        i = self.size - 1
        while i and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)
    def minheapify(self,i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l<self.size and self.arr[l] < self.arr[i]:
            smallest = l
        if r<self.size and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.minheapify(smallest)
    def extract_min(self):
        if self.size <= 0:
            return float('inf')
        if self.size == 1:
            self.size -= 1
            return self.arr[0]
        elem = self.arr[0]
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self.minheapify(0)
        return elem
    def decrease_key(self,i,x):
        if x > self.arr[i]:
            return
        self.arr[i] = x
        while i and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)
    def delete(self,i):
        self.decrease_key(i,float('-inf'))
        self.extract_min()
        self.size -= 1
    def delete(self, i):
        if i < 0 or i >= self.size:
            return  
        self.arr[i] = self.arr[self.size - 1]
        self.size -= 1
        if i < self.size:
            self.minheapify(i)
    def build_heap(self):
        for i in range((self.size-2)//2,-1,-1):
            self.minheapify(i)


    
    


        
    

h = heap(10)
h.insert(36)
h.insert(15)
h.insert(12)
h.insert(45)
h.insert(24)
h.insert(58)

# print("Heap before calling minheapify:")
# h.show()
# h.arr[0] = 50  
# print("\nHeap after manually modifying the root (violation of heap property):")
# h.show()
# h.minheapify(0)
# print("\nHeap after calling minheapify:")
# h.show()


# print("Heap before extracting min:")
# h.show()
# # Extract min and display the result
# print("\nExtracted min:", h.extract_min())
# print("Heap after extracting min:")
# h.show()
# while h.size > 0:
#         print("\nExtracted min:", h.extract_min())
#         print("Heap after extracting min:")
#         h.show()

# print("Heap before decreasing key:")
# h.show()
# h.decrease_key(2, 5)
# print("\nHeap after decreasing key:")
# h.show()



# print("Heap before deletion:")
# h.show()
# index_to_delete = 2
# print(f"\nDeleting element at index {index_to_delete} (value: {h.arr[index_to_delete]})")
# h.delete(index_to_delete)
# print("Heap after deletion:")
# h.show()


print("Heap before calling build_heap:")
h.show()
h.build_heap()
print("\nHeap after calling build_heap:")
h.show()

# insert - O(logN)
# min heapify - O(logN), extract min - O(logN)
# Decrease key - O(logN), delete - O(logN), build heap = O(N)
# height(h) of a complete binary tree - logN