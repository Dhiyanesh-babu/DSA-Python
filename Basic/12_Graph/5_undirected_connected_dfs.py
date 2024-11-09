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


    def iterative_dfs(self,s):
        stack = deque([s])
        while stack:
            node = stack.pop()
            if not self.visited[node]:
                self.visited[node] = True
                print(node)
            for neighbour in self.data[node]:
                if not self.visited[neighbour]:
                    stack.append(neighbour)

    def recursice_dfs(self,s):
        self.visited[s] = True
        print(s)
        for neighbour in self.data[s]:
            if not self.visited[neighbour]:
                self.recursice_dfs(neighbour)

            


obj = graph(7)
obj.add_edge(0,1)
obj.add_edge(0,2)
obj.add_edge(0,5)
obj.add_edge(1,3)
obj.add_edge(2,4)
obj.add_edge(3,5)
obj.add_edge(4,5)
obj.show()
obj.iterative_dfs(0)
print('-----------')
obj.visited = [False] * obj.v
obj.recursice_dfs(0)

# time O(v+e)
# space O(v+e)
# for both recursive and iterative






















