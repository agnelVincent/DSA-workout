class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self , vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return 
        return 'vertex already exists'
        
    def add_edge(self , vertex , edge):
        if vertex not in self.adj_list:
            self.add_vertex(vertex)
        if edge not in self.adj_list:
            self.add_vertex(edge)
        self.adj_list[vertex].append(edge)
    
    def bfs(self , vertex):
        if vertex not in self.adj_list:
            return False
        from collections import deque
        visited = set()
        queue = deque(vertex)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex , end=' ')
                visited.add(vertex)
            queue.extend([edge for edge in self.adj_list[vertex] if edge not in visited])
        print()
    
    def dfs(self , vertex):
        if vertex not in self.adj_list:
            return False
        
        visited = set()

        def dfs_recursive(vertex):
            if vertex not in visited:
                print(vertex , end= ' ')
                visited.add(vertex)
            for edge in self.adj_list[vertex]:
                if edge not in visited:
                    dfs_recursive(edge)
        
        return dfs_recursive(vertex)
    
    def cycle_detection(self):

        visited = set()
        rec_stack = set()

        def dfs(v):
            visited.add(v)
            rec_stack.add(v)

            for edge in self.adj_list[v]:
                if edge not in visited:
                    if dfs(edge):
                        return True
                elif edge in rec_stack:
                    return True
            
            rec_stack.remove(v)
            return False

        for vertex in self.adj_list:
            if vertex not in visited:
                if dfs(vertex):
                    return True
        return False

    
graph = Graph()

graph.add_edge('A','B',directed = True)
graph.add_edge('B','C',directed = True)
graph.add_edge('C','D',directed = True)
graph.add_edge('D','A',directed = True)

graph.bfs('A')
graph.dfs('A')
print()
print(graph.cycle_detection())


            