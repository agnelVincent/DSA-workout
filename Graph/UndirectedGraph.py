class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def insert_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print(f"Vertex '{vertex}' already exists.")

    def insert_edges(self, v1, v2):
        if v1 == v2:
            print("Self-loops are not allowed.")
            return

        if v1 not in self.adj_list:
            self.insert_vertex(v1)
        if v2 not in self.adj_list:
            self.insert_vertex(v2)

        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
        if v1 not in self.adj_list[v2]:
            self.adj_list[v2].append(v1)

    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} : {edges}")
        print(self.adj_list)



graph = UndirectedGraph()
graph.insert_vertex('A')
graph.insert_edges('A', 'B')
graph.insert_edges('A', 'C')
graph.insert_edges('C', 'D')
graph.insert_edges('B', 'D')
graph.insert_edges('A', 'B')  
graph.insert_edges('A', 'A')  
graph.display()
