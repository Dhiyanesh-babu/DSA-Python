class naive_pattern_search:
    def __init__(self,txt,pat) -> None:
        self.txt = txt
        self.pat = pat
    def search_pattern(self):
        t = len(self.txt)
        p = len(self.pat)
        for i in range(t-p+1):
            m = 0
            for j in range(p):
                if self.pat[j] == self.txt[j+i]:
                    m += 1
            if m == p: print(i)
# Time O((t-p-1)*p)

class pattern_search:
    def __init__(self,txt,pat) -> None:
        self.txt = txt
        self.pat = pat
    def search_pattern(self):
        t = len(self.txt)
        p = len(self.pat)
        i = 0
        while(i<t-p):
            count = 0
            for j in range(p):
                if self.pat[j] == self.txt[j+i]:
                    count += 1
            if count == p:
                print(i)
            if count == 0:
                i += 1
            else:
                i += count
# Time O(n)

txt = 'ABCABCDABCA'
pat = 'ABC'
obj = pattern_search(txt,pat)
obj.search_pattern()