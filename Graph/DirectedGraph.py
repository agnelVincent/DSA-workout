class Graph:
    def __init__(self):
        self.adj_list = {}

    def insert_vertex(self , vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return
        print('vertex already exists')
        return
    
    def insert_edges(self , ed1 , ed2):
        if ed1 not in self.adj_list:
            self.insert_vertex(ed1)
        if ed2 not in self.adj_list:
            self.insert_vertex(ed2)

        self.adj_list[ed1].append(ed2)
        self.adj_list[ed2].append(ed1)
        return
    
    def display(self):
        for i in self.adj_list.keys():
            print(f'{i} : {self.adj_list[i]}')

graph = Graph()
graph.insert_vertex('A')
graph.insert_edges('A','B')
graph.insert_edges('A','C')
graph.insert_edges('C','D')
graph.insert_edges('B','D')
graph.display()