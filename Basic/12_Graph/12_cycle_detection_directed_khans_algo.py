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
    
    def cycle_detecion(self):
        count  = 0
        q = deque()
        for i,a in enumerate(self.indegree):
            if not a:
                q.appendleft(i)
        while q:
            u = q.pop()
            for adj in self.data[u]:
                self.indegree[adj] -= 1
                if not self.indegree[adj]:
                    q.appendleft(adj)
            count += 1
        return count != self.v

obj = graph(5)
obj.add_edge(0,1)
obj.add_edge(1,2)
obj.add_edge(2,3)
obj.add_edge(3,1)
obj.add_edge(4,1)
 
ans = obj.cycle_detecion()
print(ans)

# time O(v+e)