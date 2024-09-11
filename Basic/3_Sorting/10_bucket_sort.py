class bucket_sort_array:
    def bucket_sort(self, arr, n, k):
        max_val = max(arr) + 1
        buckets = [[] for _ in range(k)]
        for a in arr:
            index = (k * a) // max_val
            buckets[index].append(a)
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(sorted(bucket))

        for i in range(n):
            arr[i] = sorted_arr[i]


sample = [20,88,70,85,75,95,18,82,60]
n = len(sample)
k = 5
obj = bucket_sort_array()
obj.bucket_sort(sample, n, k)
print(sample)

# time best - O(N), worst - all in same bucket O(N^2) this is for sorting

