# naive approach

class reverse:
    def __init__(self,data) -> None:
        self.data = data
        self.ans = []
    def reverse_string(self):
        for i in range(len(self.data)-1,-1,-1):
            self.ans.append(self.data[i])
        return self.ans


sample = [10,5,7,30]
obj = reverse(sample)
ans = obj.reverse_string()
print(ans)

    
# Time - O(N)
# Space - O(N)






# Efficient method


class reverse:
    def __init__(self,data) -> None:
        self.data = data
    def reverse_string(self):
        low = 0
        high = len(self.data)-1
        while(low<high):
            self.data[low], self.data[high] = self.data[high], self.data[low]
            low+=1
            high-=1
        return self.data



sample = [10,5,7,30]
obj = reverse(sample)
ans = obj.reverse_string()
print(ans)


#  use data.reverse() or data[:] = data[::] alternatives