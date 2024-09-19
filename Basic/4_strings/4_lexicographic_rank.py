import math

class lexicographic_rank:
    def find(self, data, n):
        rank = 1
        mul = math.factorial(n)
        count = [0]*256
        for a in data:
            count[ord(a)] +=1
        for i in range(1, 256):
            count[i] = count[i] + count[i-1]
        for i in range(n):
            mul = mul//(n-i)
            rank = rank + count[ord(data[i])-1]*mul
            for j in range(ord(data[i]),256):
                count[j] -= 1
        return rank
# Time O(N)
# SPace O(1) - we take extra space, but constant space of 256
        
sample = 'STRING'
n =  len(sample)
obj = lexicographic_rank()
ans = obj.find(sample, n)
print(ans)
