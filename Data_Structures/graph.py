class Vertex:
    def __init__(self, value):
        self.value = value
        self.in_edges, self.out_edges = [], []
    
class Edge:
    def __init__(self, from_vertex, to_vertex, cost=1):
        self.from_vertex, self.to_vertex, self.cost = from_vertex, to_vertex, cost
        from_vertex.out_edges.append(self)
        to_vertex.in_edges.append(self)

    def destroy(self):
        self.from_vertex.out_edges.remove(self)
        self.to_vertex.in_edges.remove(self)
        self.from_vertex, self.to_vertex = None, None
