import random
# Using QueueWithMax simply to test it and RingBuffer and StaticArray
# O(n) (I think because there are O(1) vertices per edge since acyclic)
from Data_Structures.graph import Vertex, Edge
from Data_Structures.queue_with_max import Queue
def topological_sort_khan(vertices):
    in_edge_counts = {}
    queue = Queue()

    for v in vertices:
        in_edge_counts[v] = len(v.in_edges)
        if len(v.in_edges) == 0:
            queue.enqueue(v)

    sorted_vertices = []

    while queue:
        vertex = queue.dequeue()
        sorted_vertices.append(vertex)

        for edge in vertex.out_edges:
            to_vertex = edge.to_vertex
            in_edge_counts[to_vertex] -= 1
            if in_edge_counts[to_vertex] == 0:
                queue.enqueue(to_vertex)
    if len(sorted_vertices) != len(vertices):
        return [] # Cycle detected. No ordering possible
    return sorted_vertices

def topological_sort_tarjan(vertices):
    order = [] # we could use only this array and not the explored set and then check in this array each time
    # but then we don't have the O(1) time lookup that we get from the explored set
    explored = set() 
    cycle_tracker = set()
    cycle = False

    for vertex in vertices:
        if not vertex in explored:
            cycle = dfs(vertex, explored, cycle_tracker, order, cycle)  
        if cycle: return [] 
    return list(reversed(order))


def dfs(vertex, explored, cycle_tracker, order, cycle):
    if vertex in cycle_tracker: return True
    cycle_tracker.add(vertex)

    for edge in vertex.out_edges:
        next_vertex = edge.to_vertex
        if not next_vertex in explored:
            cycle = dfs(next_vertex, explored, cycle_tracker, order, cycle) 
        if cycle:
            return True 

    explored.add(vertex)
    cycle_tracker.remove(vertex)
    order.append(vertex)
    return False

v1 = Vertex("Wash Markov") 
v2 = Vertex("Feed Markov") 
v3 = Vertex("Dry Markov") 
v4 = Vertex("Brush Markov") 
v5 = Vertex("Cuddle Markov") 
v6 = Vertex("Walk Markov") 
v7 = Vertex("Teach Markov") 
v8 = Vertex("Worship Markov") 
vertices = [v1, v2, v3, v4, v5, v6, v7, v8]
random.shuffle(vertices)
Edge(v1, v2) # Wash -> Feed
Edge(v1, v3) # Wash -> Dry
Edge(v2, v4) # Feed -> Brush
Edge(v3, v4) # Dry -> Brush
Edge(v2, v5) # Feed -> Cuddle
Edge(v4, v6) # Brush -> Walk
Edge(v5, v6) # Cuddle -> Walk
Edge(v6, v7) # Walk -> Teach
Edge(v7, v8) # Teach -> Worship

print([v.value for v in topological_sort_khan(vertices)])
print([v.value for v in topological_sort_tarjan(vertices)])

# Test cyclic case (should return [])
v1 = Vertex("Wash Markov")
v2 = Vertex("Feed Markov")
v3 = Vertex("Dry Markov")
v4 = Vertex("Brush Markov")
v5 = Vertex("Cuddle Markov")
v6 = Vertex("Walk Markov")
v7 = Vertex("Teach Markov")
v8 = Vertex("Worship Markov")
vertices = [v1, v2, v3, v4, v5, v6, v7, v8]
random.shuffle(vertices)
Edge(v1, v2)
Edge(v1, v3)
Edge(v2, v4)
Edge(v3, v4)
Edge(v2, v5)
Edge(v4, v6)
Edge(v5, v6)
Edge(v6, v7)
Edge(v7, v8)
Edge(v8, v2)

print([v.value for v in topological_sort_khan(vertices)])
print([v.value for v in topological_sort_tarjan(vertices)])
