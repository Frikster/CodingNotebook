# Given an Array of tuples, where tuple[0] represents a package id, and tuple[1] 
# represents its dependency, determine the order in which the packages should be installed. 
# Only packages that have dependencies will be listed, but all packages from 1..max_id exist.
# N.B. this is how npm works.
from Data_Structures.graph import Vertex, Edge
from App_Academy.topological_sort import topological_sort_khan

def install_order(arr):
    max_id = 0
    vertices = {}
    for tup in arr:
        # create the graph
        if not tup[0] in vertices:
            vertices[tup[0]] = Vertex(tup[0]) 
        if not tup[1] in vertices:
            vertices[tup[1]] = Vertex(tup[1])
        Edge(vertices[tup[1]], vertices[tup[0]]) # dependency needs to be installed first
        # reset max_id if needed
        if max(tup) > max_id: max_id = max(tup) 

    # find the missing packages (i.e. ones with no dependencies)
    independent = []
    for id in range(1, max_id):
        if not id in vertices:
            independent.append(id)

    # sort the vertices of the graph and add the missing packages
    return independent + [v.value for v in topological_sort_khan(vertices.values())]

arr = [[3, 1], [2, 1], [6, 5], [3, 6], [3, 2], [4, 3], [9, 1]]
print(install_order(arr))
arr = [[3, 1], [2, 1], [6, 5], [3, 6], [3, 2], [4, 3], [9, 1]]
print(install_order([[3, 1], [2, 1], [6, 5], [3, 6], [3, 2], [4, 3], [9, 1]]))