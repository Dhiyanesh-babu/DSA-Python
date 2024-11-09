from collections import deque

class graph:
    def __init__(self,v) -> None:
        self.v = v
        self.indegree = [0]*v
        self.data = [[] for _ in range(v)]
    
    def show(self):
        for i in range(self.v):
            print(i,'->',self.data[i])
    
    def add_edge(self,u,v):
        self.data[u].append(v)
        self.indegree[v] += 1
    
    def topological_sort_bfs(self):
        q = deque()
        for i,a in enumerate(self.indegree):
            if not a:
                q.appendleft(i)
        while q:
            u = q.pop()
            print(u)
            for adj in self.data[u]:
                self.indegree[adj] -= 1
                if not self.indegree[adj]:
                    q.appendleft(adj)

obj = graph(5)
obj.add_edge(0,2)
obj.add_edge(0,3)
obj.add_edge(2,3)
obj.add_edge(1,3)
obj.add_edge(1,4)
obj.topological_sort_bfs()

# time O(v+e)

    
