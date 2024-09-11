class radix_sort_array:
    def counting_sort(self, arr, n, exp):
        count = [0]*10
        for a in arr:
            count[(a//exp)%10] += 1
        for i in range(1,10):
            count[i] = count[i] + count[i-1]
        output = [None]*n
        for i in range(n-1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(n):
            arr[i] = output[i]
        
    def radix_sort(self, arr, n):
        max_elem = max(arr)
        exp = 1
        while(max_elem/exp > 0):
            self.counting_sort(arr, n, exp)
            exp *= 10


sample = [319,212,6,8,100,50]
n = len(sample)
obj = radix_sort_array()
obj.radix_sort(sample,n)
print(sample)

# Time Theta(d*(n+b)), Space Theta (n+b)
# d- number of nigits, b= 10
# Increse in b <=> Decrease in Time <=> Increase in space
