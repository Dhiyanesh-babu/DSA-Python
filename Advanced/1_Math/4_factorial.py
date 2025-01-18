class solution:
    def __init__(self,n) -> None:
        self.n = n
    def fact(self):
        def helper(n):
           if n == 1:
               return 1
           return n*helper(n-1)
        return helper(self.n)

sample = 5
obj = solution(sample)
print(obj.fact())

        