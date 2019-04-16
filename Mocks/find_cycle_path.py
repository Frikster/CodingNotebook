class node:
    def __init__(val, out_nodes, in_nodes):
        self.val = val
        self.out_nodes = out_nodes 
        self.in_nodes = in_nodes

def find_cycle_path(node):
    return find_cycle_path_helper(node, node, [])

def find_cycle_path_helper(node, end_node, path):
    if node is end_node and path!=[]: return path   
    for out_node in node.out_nodes:
        res = find_cycle_path_helper(out_node, end_node, path+[out_node])
        if res: return res      
    return


node: node1
end_node: node1
path[node2, node1]


node: node2
end_node: node1
path [node2, node1]
node.out_nodes[node1]


node.out_nodes [node2, node3]

node1 -> node2 -> node1 
      -> node3 -> node4
