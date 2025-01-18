class solution:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def gcd_naive(self):
        res = min(self.a, self.b)
        while res:
            if not self.a % res and not self.b % res:
                break
            res -= 1
        return res

    def gcd_opt1(self):
        while self.a != self.b:
            if self.a > self.b:
                self.a -= self.b
            else:
                self.b -= self.a
        return self.a

    @staticmethod
    def gcd_opt2(a, b):
        if b == 0:
            return a
        return solution.gcd_opt2( b, a % b)

    @staticmethod
    def gcd_opt3(a, b):
        if b == 0:
            return a
        else:
            return solution.gcd_opt2(b, a % b)

a = 12
b = 15
obj = solution(a, b)
print(obj.gcd_naive())
print(obj.gcd_opt1())
print(obj.gcd_opt2(a, b))
print(solution.gcd_opt3(a, b))

    
        

        