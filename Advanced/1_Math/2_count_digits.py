class solution:
    def __init__(self,n) -> None:
        self.n = n
    def count(self):
        ans = 0
        while self.n:
            self.n = self.n // 10
            ans += 1
        return ans

sample = 456
obj = solution(sample)
ans = obj.count()
print(ans)