class Graph:

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self , vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self , vertex , edge):
        if vertex not in self.adj_list:
            self.add_vertex(vertex)
        if edge not in self.adj_list:
            self.add_vertex(edge)
        self.adj_list[vertex].append(edge)
        self.adj_list[edge].append(vertex)

    def bfs(self , vertex):
        if vertex not in self.adj_list:
            return False
        
        from collections import deque
        queue = deque(vertex)
        visited = set()

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex ,end=' ')
                visited.add(vertex)
                for i in self.adj_list[vertex]:
                    queue.append(i)
        print()

    def dfs(self , vertex):
        
        if vertex not in self.adj_list:
            return False
        
        visited = set()

        def dfs_recursive(vertex):
            print(vertex , end = ' ')
            visited.add(vertex)
            for i in self.adj_list[vertex]:
                if i not in visited:
                    dfs_recursive(i)

        return dfs_recursive(vertex)
    
    def cycle_detection(self):

        visited = set()

        def cycle(vertex , parent = None):
            visited.add(vertex)
            for i in self.adj_list[vertex]:
                if i not in visited:
                    if cycle(i , vertex):
                        return True
                elif i != parent:
                    return True
            return False

        for i in self.adj_list:
            if i not in visited:
                if cycle(i):
                    return True
        return False
        


graph = Graph()
graph.add_edge('A','B')
graph.add_edge('B','C')
graph.add_edge('C','D')
graph.add_edge('D','A')

graph.bfs('A')

graph.dfs('A')
print()

print(graph.cycle_detection())