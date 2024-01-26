# better approach
import time

class rotate:
    def __init__(self,data) -> None:
        self.data = data
    def left_rotate(self):
        temp = self.data[0]
        for i in range(1,len(self.data)):
            self.data[i-1] = self.data[i]
        self.data[len(self.data)-1] = temp

        return self.data
sample = [1,2,3,4,5]
obj = rotate(sample)
ans = obj.left_rotate()
print(ans)


# Time O(N)
# Space O(N








# Efficient approach
class rotate:
    def __init__(self,data) -> None:
        self.data = data
    def left_rotate(self):
        self.data = self.data[1:] + [self.data[0]]

        return self.data
sample = [1,2,3,4,5]
obj = rotate(sample)
ans = obj.left_rotate()
print(ans)

