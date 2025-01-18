
import math
class digits:
    def __init__(self,n) -> None:
        self.n = n
    def naive1(self):
        count = 0
        while self.n:
            self.n = self.n//10
            count += 1
        return count
    def naive2(self, num = None):
        if num is None:
            num = self.n
        if num == 0:
            return 0
        return 1 + self.naive2(num//10)
    def efficient(self):
        if n == 0:
            return 1
        return math.floor(math.log10(abs(n))+1)
    
n = 564
obj = digits(n)
ans = obj.naive2()
print(ans)
