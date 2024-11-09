from collections import deque


class graph:
    def __init__(self,v) -> None:
        self.data = [[] for _ in range(v)]
        self.v = v
        self.visited = [False]*self.v

    def show(self):
        for i,a in enumerate(self.data):
            print(i,'->',a)

    def add_edge(self,u,v):
        self.data[u].append(v)
        self.data[v].append(u)

    def bfsd(self):
        for i,a in enumerate(self.visited):
            if not a:
                self.bfs(i)

    
    def bfs(self,s):
        q = deque()
        q.append(s)
        self.visited[s] = True
        while(q):
            temp = q.popleft()
            print(temp)
            for a in self.data[temp]:
                if not self.visited[a]:
                    self.visited[a] = True
                    q.append(a)


obj = graph(7)
obj.add_edge(0,1)
obj.add_edge(0,2)
obj.add_edge(1,3)
obj.add_edge(2,3)
obj.add_edge(4,5)
obj.add_edge(4,6)
obj.add_edge(5,6)
obj.show()
obj.bfsd()
    

