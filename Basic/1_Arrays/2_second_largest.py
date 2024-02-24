

# Naive -Two iterations

class SecondLargest:
    def __init__(self,sample) -> None:
        self.nums = sample
    def second_largest(self):
        largest = max(self.nums, default=None)
        second_largest = float('-inf')
        for a in  self.nums:
            if a > second_largest and a!=largest:
                second_largest = a
        return second_largest
    
sample = [1,12,3,9,8,7,11,2,5,6,7]
obj = SecondLargest(sample)
ans = obj.second_largest()
print(ans)

# Time - O(N)
# Space - O(1)








# Optimised - One iteration

class SecondLargest:
    def __init__(self,sample) -> None:
        self.nums = sample
    def second_largest(self):
        second_lrgest = float('-inf')
        largest = float('-inf')
        for a in self.nums:
            if a > largest:
                second_lrgest = largest
                largest = a
            elif a!= largest: # to handle duplicate elements
                if a > second_lrgest:
                    second_lrgest = a
        return second_lrgest


    
sample = [1,12,3,9,8,7,11,2,5,6,7]
obj = SecondLargest(sample)
ans = obj.second_largest()
print(ans)


# Time - O(N)
# Space - O(1)
