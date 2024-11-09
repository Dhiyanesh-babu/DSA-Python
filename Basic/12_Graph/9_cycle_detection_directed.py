class graph:
    def __init__(self,v) -> None:
        self.data = [[] for _ in range(v)]
        self.v = v
        self.visited = [False]*v
        self.recst = [False]*v
    
    def add_edge(self,u,v):
         self.data[u].append(v)


    def show(self):
        for i in range(self.v):
            print(i,'->',self.visited[i])

    def dfs_rec(self,s):
        self.visited[s] = True
        self.recst[s] = True
        for adj in self.data[s]:
            if not self.visited[adj]:
                if self.dfs_rec(adj):
                    return True
            elif self.recst[adj]:
                return True
        self.recst[s] = False
        return False

    def dfs(self):
        for i in range(self.v):
            if not self.visited[i]:
                if self.dfs_rec(i):
                    return True
        return False
    

obj = graph(6)
obj.add_edge(0,1)
obj.add_edge(2,1)
obj.add_edge(2,3)
obj.add_edge(3,4)
obj.add_edge(4,5)
obj.add_edge(5,3)
ans = obj.dfs()
print(ans)

# time O(v+e)