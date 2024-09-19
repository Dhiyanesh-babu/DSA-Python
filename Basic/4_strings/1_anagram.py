class anagram:
    def check(self,s1,s2):
        if len(s1) != len(s2):
            return False
        count = [0]*256
        for a in s1:
            count[ord(a)] += 1
        for a in s2:
            count[ord(a)] -= 1
        for i in count:
            if i != 0:
                return False
        return True
        
s1 = 'geeks'
s2 = 'ekegs'
obj = anagram()
print(obj.check(s1,s2))


