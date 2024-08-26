
from typing import List
from numpy import inf


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        smallest_word = strs[0]
        smallest_length = inf
        for i in range(len(strs)):
            if len(strs[i]) < smallest_length:
                smallest_length = len(strs[i])
                smallest_word = strs[i]
        strs.remove(smallest_word)
        if len(strs) == 0:
            return smallest_word
        #print(smallest_word)
        for i in range(smallest_length):
            
            flag = True
            temp = smallest_word[0:i+1]
            print(temp)
            for b in strs:
                if b[0:i] != temp:
                    flag = False
            if flag == True:
                ans = temp
                
        return ans
    

obj = Solution()
soln = obj.longestCommonPrefix(["ab", "a"])
print(soln)