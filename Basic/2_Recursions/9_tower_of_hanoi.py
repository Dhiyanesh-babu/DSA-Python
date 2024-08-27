class tower_of_hanoi:
    def __init__(self, data, a, b, c) -> None:
        self.n = data
        self.a = a
        self.b = b
        self.c = c
    def tower(self):
        if (self.n == 1):
            print(f"Move from {self.a} to {self.c}")
            return
        tower_of_hanoi(self.n-1, self.a, self.c, self.b).tower()
        print(f"move from {self.a} to {self.c}")
        tower_of_hanoi(self.n-1, self.b, self.a, self.c).tower()

sample = 3
a = 'a'
b = 'b'
c= 'c'

obj = tower_of_hanoi(3, a, b, c)
obj.tower()























