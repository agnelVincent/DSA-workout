class Graph:
    def __init__(self):
        self.adj_list = {}

    def insert_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def insert_edges(self, vertex, edge):
        self.insert_vertex(vertex)
        self.insert_vertex(edge)

        if edge not in self.adj_list[vertex]:  
            self.adj_list[vertex].append(edge)

    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} : {edges}")
