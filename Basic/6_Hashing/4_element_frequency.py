from collections import Counter

class element_frequency:
    def find(self, arr):
        count = Counter(arr)
        print(count)

sample = [10,12,13,12,14,14,16,17,16]
obj = element_frequency()
obj.find(sample)

