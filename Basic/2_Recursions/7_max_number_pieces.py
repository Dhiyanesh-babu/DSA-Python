class MaxPieces:
    def __init__(self, n: int, a: int, b: int, c: int):
        self.n = n
        self.a = a
        self.b  = b
        self.c = c
    def calculate_max_pieces(self) -> int:
        if self.n < 0:
            return -1
        if self.n == 0:
           return 0
        return max(MaxPieces(self.n-self.a,self.a,self.b,self.c).calculate_max_pieces(),MaxPieces(self.n-self.b,self.a,self.b,self.c).calculate_max_pieces(),MaxPieces(self.n-self.c,self.a,self.b,self.c).calculate_max_pieces())+1

sample = 23
a = 12
b = 9 
c = 11 
obj = MaxPieces(sample,a,b,c)
ans = obj.calculate_max_pieces()
print(ans)


# Time O(3^N)
# space O(3)