class heap_sort_array:
    def heapify(self, arr, n, i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr,n, largest )

    def buildheap(self, arr, n):
        for i in range((n-2)//2, -1, -1):
            self.heapify(arr, n, i)
    
    def heap_sort(self, arr, n):
        self.buildheap(arr,n)
        for j in range(n-1, 0, -1):
            arr[0], arr[j] = arr[j], arr[0]
            self.heapify(arr, j, 0)


sample = [10,15,50,4,20]
n = len(sample)
obj = heap_sort_array()
obj.heap_sort(sample, n)
print(sample)


