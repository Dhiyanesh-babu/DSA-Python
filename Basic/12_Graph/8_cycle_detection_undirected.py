from collections import deque


class graph:
    def __init__(self,v) -> None:
        self.data = [[] for _ in range(v)]
        self.v = v
        self.visited = [False] * self.v

    def show(self):
        for i,a in enumerate(self.data):
            print(i,'->',a)

    def add_edge(self,u,v):
        self.data[u].append(v)
        self.data[v].append(u)


    def recursice_dfs(self,s,parent):
        self.visited[s] = True
        for adj in self.data[s]:
            if not self.visited[adj]:
                if self.recursice_dfs(adj,s):
                    return True
            elif adj != parent:
                return True
        return False

    def rec_dfs(self):
        for i in range(self.v):
            if not self.visited[i]:
                if self.recursice_dfs(i,-1):
                    return True
        return False

            


obj = graph(6)
# obj.add_edge(0,1)
# obj.add_edge(1,2)
# obj.add_edge(2,3)
# obj.add_edge(1,3)
# obj.add_edge(2,4)
# obj.add_edge(4,5)
obj.add_edge(0,1)
obj.add_edge(3,4)
obj.add_edge(4,5)
obj.add_edge(5,3)
obj.show()
ans = obj.rec_dfs()
print(ans)

# Time O(v+e)