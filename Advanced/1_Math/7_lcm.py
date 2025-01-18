class  solution:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    
    def lcm_naive(self):
        res = max(self.a, self.b)
        while 1:
            if res%self.a == 0 and res%self.b == 0:
                return res
            res += 1
        return
    
    @staticmethod
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return solution.gcd(b, a % b)
    
    def lcm_opt(self):
        gcd = solution.gcd(self.a, self.b)
        return (self.a*self.b)//(gcd)

a= 12
b= 15
obj = solution(a,b)
print(obj.lcm_naive())
print(obj.lcm_opt())
