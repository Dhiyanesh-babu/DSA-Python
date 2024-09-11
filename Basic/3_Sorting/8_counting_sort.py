class counting_sort_array:
    def naive(sellf, arr, n, k):
        count = [0]*k
        for a in arr:
            count[a] += 1
        index = 0
        for i,a in enumerate(count):
            for j in range(a):
                arr[index] = i
                index += 1
    def optimised(self, arr, n, k):
        count = [0]*k
        for a in arr:
            count[a] += 1
        for i in range(1, k):
            count[i] = count[i] + count[i-1]
        output = [None]*n
        for i in range(n-1, -1, -1):
            output[count[arr[i]]-1] = arr[i]
            count[arr[i]] -= 1
        for i in range(n):
            arr[i] = output[i]



sample = [1,4,4,1,0,1]
n = len(sample)
k = max(sample)+1
obj = counting_sort_array()
obj.optimised(sample, n, k)
print(sample)

# Time and space Theta(N+K)