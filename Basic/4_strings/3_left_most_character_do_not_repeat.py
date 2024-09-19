class not_repeating:
    def find(self, data):
        count = [-1]*256
        for i,a in enumerate(data):
            if count[ord(a)] == -1:
                count[ord(a)] = i
            else:
                count[ord(a)] = -2
        ans = float('inf')
        for i in count:
            if i >= 0:
                ans = min(ans, i)
        return -1 if ans == float('inf') else ans
# Time O(N)

sample = 'aabbcc'
obj = not_repeating()
ans = obj.find(sample)
print(ans)



