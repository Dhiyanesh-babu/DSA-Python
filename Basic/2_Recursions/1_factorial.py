# naive approach

class factorial:
    def __init__(self,data) -> None:
        self.num = data
    def find_factorial(self):
        if self.num == 1:
            return 1
        return self.num * factorial(self.num-1).find_factorial()
    
sample = 4
obj = factorial(sample)
ans =  obj.find_factorial()
print(ans)

# Time : O(N)
# Space : O(N)







# efficient approach

class factorial:
    def __init__(self,data) -> None:
        self.num = data
        self.ans = 1
    def find_factorial(self):
        for i in range(self.num,1,-1):
            self.ans *= i
        return self.ans

    
sample = 4
obj = factorial(sample)
ans =  obj.find_factorial()
print(ans)

# Time - O(N)
# Space - O()