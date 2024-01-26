class DigitsSum:
    def __init__(self,data) -> None:
        self.num = data
    def calculate_sum(self):
        if self.num<10:
            return self.num
        return DigitsSum(self.num//10).calculate_sum() + self.num%10

data = 253    
obj = DigitsSum(253)
ans = obj.calculate_sum()
print(ans)


# Time O(d)
# Space O(d) d -> len(number)