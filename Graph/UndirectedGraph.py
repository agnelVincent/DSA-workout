class Graph:
    def __init__(self):
        self.adj_list = {}

    def insert_vertex(self , vertex):
        if vertex in self.adj_list:
            print('Vertex already exists')
            return
        
        self.adj_list[vertex] = []

    def insert_edges(self , vertex , edge):
        if vertex not in self.adj_list:
            self.insert_vertex(vertex)

        if edge not in self.adj_list:
            self.insert_vertex(edge)

        self.adj_list[vertex].append(edge)

    def display(self):
        for i in self.adj_list.keys():
            print(f'{i} : {self.adj_list[i]}')


graph = Graph()
graph.insert_vertex('A')
graph.insert_edges('A','B')
graph.insert_edges('B','C')
graph.display()