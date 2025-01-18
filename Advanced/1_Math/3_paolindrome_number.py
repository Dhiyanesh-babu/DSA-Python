class solution:
    def __init__(self,n) -> None:
        self.n = n
    def find(self):
        rev = 0
        temp = self.n
        while temp:
            digit = temp % 10
            rev = (rev*10) + digit
            temp = temp // 10
        return rev == self.n

sample = 78987
obj = solution(sample)
print(obj.find())
