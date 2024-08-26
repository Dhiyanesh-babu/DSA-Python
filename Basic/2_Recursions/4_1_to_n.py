class n_to_1:
    def __init__(self, data) -> None:
        self.num = data

    def show(self):
        if self.num == 0:
            return 0
        n_to_1(self.num - 1).show()
        print(self.num)


sample = 5
obj = n_to_1(sample)
obj.show()
## hi hi
