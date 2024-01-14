
class n_to_1:
    def __init__(self,data) -> None:
        self.num = data
    def show(self):
        if self.num == 0:
            return 0
        print(self.num)
        n_to_1(self.num-1).show()

sample = 5
obj = n_to_1(sample)
obj.show()

# Time - O(N)
# Space - O(N)
# This is tail recursive. its better

# better approach to use iterative loop to prevent recursice stack to reduce space
