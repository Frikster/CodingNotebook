from Data_Structures.graph import Vertex, Edge
# TODO: Test
# TODO: using actual queue
# O(n) (I think because there are O(1) vertices per edge since acyclic)
def topological_sort_khan(vertices):
    in_edge_counts = {}
    queue = []

    for v in vertices:
        in_edge_counts[v] = len(v.in_edges)
        if len(v.in_edges) == 0:
            queue.append(v)

    sorted_vertices = []

    while queue:
        vertex = queue.pop(0)
        sorted_vertices.append(vertex)

        for edge in vertex.out_edges:
            to_vertex = edge.to_vertex
            in_edge_counts[to_vertex] -= 1
            if in_edge_counts[to_vertex] == 0:
                queue.append(to_vertex)
    if len(sorted_vertices) != len(vertices):
        return [] # Cycle detected. No ordering possible
    return sorted_vertices

def topological_sort_tarjan(vertices):
    order = []
    explored = set()
    temp = set()
    cycle = False

    for vertex in vertices:
        if not vertex in explored:
            cycle = dfs(vertex, explored, temp, order, cycle)  
        if cycle: return [] 
    return list(reversed(order))


def dfs(vertex, explored, temp, order, cycle):
    if vertex in temp: return True
    temp.add(vertex)

    for edge in vertex.out_edges:
        next_vertex = edge.to_vertex
        if not next_vertex in explored:
            cycle = dfs(next_vertex, explored, temp, order, cycle) 
        if cycle:
            return True 

    explored.add(vertex)
    temp.delete(vertex)
    order.append(vertex)
    return False
