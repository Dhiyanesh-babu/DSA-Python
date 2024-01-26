class palindrome:
    def __init__(self, data:str) -> None:
        self.data = data
    def check_palindrome(self) ->  bool:
        if self.data == self.data[::-1]:
            return True
        else:
            return False


sample = "madam"
obj = palindrome(sample)
ans = obj.check_palindrome()
print(ans)

# Time - O(N)
# Space - O(N )






class palindrome:
    def __init__(self, data:str) -> None:
        self.data = data
    def check_palindrome(self) ->  bool:
        low = 0
        high = len(self.data)-1
        while low<high:
            if self.data[low] == self.data[high]:
                low+=1
                high-=1
            else:
                return False
        return True




sample = "madam"
obj = palindrome(sample)
ans = obj.check_palindrome()
print(ans)


# Time - O(N)
# Space - O(1)





class palindrome:
    def __init__(self, data:str, start:int, end:int) -> None:
        self.data = data
        self.start = start 
        self.end = end
    def check_palindrome(self) ->  bool:
        if self.start >= self.end:
            return True
        if self.data[self.start] != self.data[self.end]:
            return False
        return palindrome(self.data,self.start+1,self.end-1).check_palindrome()

        


sample = "madam"
start = 0
end = len(sample)-1
obj = palindrome(sample,start,end)
ans = obj.check_palindrome()
print(ans)
