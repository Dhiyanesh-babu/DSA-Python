class left_most_char_that_repeats:
    def find(self, word):
        ans = float('inf')
        info = {}
        for i,a in enumerate(word):
            if a not in info:
                info[a] = i
            else:
                if info[a] < ans:
                    ans = info[a]
        return ans
            

sample  = 'geg'
obj = left_most_char_that_repeats()
ans = obj.find(sample)
print(ans)
# n^2 - traverse fully for each element
# 2n - use count array
# This solution is Theta(n)