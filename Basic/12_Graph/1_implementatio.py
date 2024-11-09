class list_graph:
    def __init__(self,v) -> None:
        self.v = v
        self.data = [[] for _ in range(v)]
    
    def show(self):
        for i,a in enumerate(self.data):
            print(i,'->',a)

    def add_edge(self,u, v):
        self.data[u].append(v)
        self.data[v].append(u)

obj = list_graph(4)
obj.add_edge(0,1)
obj.add_edge(0,2)
obj.add_edge(1,2)
obj.add_edge(1,3)
obj.show()

class matrix_graph:
    def __init__(self,n) -> None:
        self.matrix = [[0]*(n) for _ in range(n)]
    
    def add_edge(self,u,v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def show(self):
        print(self.matrix)

obj = matrix_graph(4)
obj.add_edge(0,1)
obj.add_edge(0,2)
obj.add_edge(1,2)
obj.add_edge(1,3)
obj.show()




















