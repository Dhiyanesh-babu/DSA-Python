from collections import deque


class graph:
    def __init__(self,v) -> None:
        self.data = [[] for _ in range(v)]
        self.v = v
        self.visited = [False] * self.v
        self.st = deque()

    def show(self):
        for i,a in enumerate(self.data):
            print(i,'->',a)

    def add_edge(self,u,v):
        self.data[u].append(v)



    def recursice_dfs(self,s):
        self.visited[s] = True
        for neighbour in self.data[s]:
            if not self.visited[neighbour]:
                self.recursice_dfs(neighbour)
        self.st.append(s)


    def topological_sort_dfs(self):
        for i in range(self.v):
            if not self.visited[i]:
                self.recursice_dfs(i)
        while self.st:
            print(self.st.pop())


            


obj = graph(5)
obj.add_edge(0,1)
obj.add_edge(1,3)
obj.add_edge(2,3)
obj.add_edge(2,4)
obj.add_edge(3,4)

#obj.show()

obj.topological_sort_dfs()

# time O(v+e)