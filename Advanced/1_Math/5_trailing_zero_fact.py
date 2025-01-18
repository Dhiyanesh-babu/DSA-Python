class solution:
    def __init__(self,n) -> None:
        self.n = n
    
    def zero_count_opt(self):
        count = 0
        i = 5
        while i <= self.n:
            count += self.n // i  
            i *= 5  
        return count
sample = 251
obj = solution(sample)
print(obj.zero_count_opt())
