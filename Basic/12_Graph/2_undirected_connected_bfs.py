from collections import deque


class graph:
    def __init__(self,v) -> None:
        self.data = [[] for _ in range(v)]
        self.v = v

    def show(self):
        for i,a in enumerate(self.data):
            print(i,'->',a)

    def add_edge(self,u,v):
        self.data[u].append(v)
        self.data[v].append(u)

    
    
    def iterative_bfs(self,s):
        visited = [False]*self.v
        q = deque()
        q.append(s)
        visited[s] = True
        while(q):
            temp = q.popleft()
            print(temp)
            for a in self.data[temp]:
                if not visited[a]:
                    visited[a] = True
                    q.append(a)



obj = graph(6)
obj.add_edge(0,1)
obj.add_edge(0,2)
obj.add_edge(0,5)
obj.add_edge(1,3)
obj.add_edge(2,4)
obj.add_edge(3,5)
obj.add_edge(4,5)
obj.show()
obj.iterative_bfs(0)
    

# time O(v+e)
# space O(v+e)