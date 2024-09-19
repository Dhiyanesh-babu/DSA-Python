
class naive_rotation:
    def __init__(self,s1,s2) -> None:
        self.s1 = s1
        self.s2 = s2
    def check_rotation(self) -> bool:
        if len(s1) != len(s2):
            return False
        ind = s2.find(s1[0])
        for i in range(len(s2)):
            print(i,ind)
            if s1[i] != s2[ind%len(s2)]:
                return False
            ind += 1
        return True
# Time O(2N) - for finding index(N) and looping(N)

class rotation:
    def __init__(self,s1,s2) -> None:
        self.s1 = s1
        self.s2 = s2
    def check_rotation(self) -> bool:
        s1 = self.s1 + self.s1
        return s2 in s1
# Time O(2N) for concatenating(N) and finding(N)


s1 = 'ABCD'
s2 = 'DBAC'
obj = rotation(s1,s2)
ans = obj.check_rotation()
print(ans)
