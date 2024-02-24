class Subset:
    def __init__(self, data: str, index: int, ans: str) -> None:
        self.data = data
        self.index = index
        self.ans = ans
    def print_substring(self):
        if (self.index==len(self.data)):
            print(self.ans)
            return
        Subset(self.data, self.index+1, self.ans).print_substring()
        Subset(self.data, self.index+1, self.ans+self.data[self.index]).print_substring()
        
        

sample = "ABC"
obj = Subset(sample,0,"")
obj.print_substring()

# Time - O(2^N)
# Space - O(2^N)