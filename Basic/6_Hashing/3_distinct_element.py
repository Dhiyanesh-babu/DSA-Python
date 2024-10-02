class disstint_elements:
    def find(self, arr):
        return set(arr)

sample = [10,12,13,12,14,14,16,17,16]
obj = disstint_elements()
ans = obj.find(sample)

print(ans)