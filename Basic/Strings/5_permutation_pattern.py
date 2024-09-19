class naive_permutation_pattern:
    def __init__(self, text, pattern) -> None:
        self.text = text
        self.pattern = pattern
    def check(self, low):
        count = [0]*256
        for i in range(len(self.pattern)):
            count[ord(self.pattern[i])] += 1
        for i in range(len(self.pattern)):
            count[ord(self.text[low+i])] -= 1
        for a in count:
            if a!= 0: 
                return False
        return True
        
    def find_pattern(self):
        for i in range(len(text)-len(pattern)+1):
            if(self.check(i)):
                return True
        return False
# Time O(O((t−p+1)×p))



class permutation_pattern:
    def __init__(self, text, pattern) -> None:
        self.text = text
        self.pattern = pattern

    def are_same(self, arr1, arr2):
        for i in range(256):
            if arr1[i] != arr2[i]:
                return False
        return True
    
    def find_pattern(self):
        p = len(self.pattern)
        t = len(self.text)
        count_txt = [0]*256
        count_pat = [0]*256
        for a in self.pattern:
            count_pat[ord(a)] += 1
        for i in range(p):
            count_txt[ord(self.text[i])] += 1
        if(self.are_same(count_pat,count_txt)):
            print('found')
            return
        for i in range(1,t-p+1):
            count_txt[ord(self.text[i-1])] -= 1
            count_txt[ord(self.text[p+i-1])] += 1
            if(self.are_same(count_pat,count_txt)):
                print('found')
                return
        print('not found')
        
# (t+p)

text = 'geeksforgeeks'
pattern = 'esk'
obj = permutation_pattern(text, pattern)
obj.find_pattern()
