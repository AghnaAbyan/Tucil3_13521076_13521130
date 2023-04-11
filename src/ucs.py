from node import Node

def fVal(adj_m, parent, node):
    return (parent.fValue + adj_m[parent.id][node])

def ucs(adj_m, s_node, g_node):
    start_node = Node(s_node, 0)
    goal_node = Node(g_node, 0)
    visited = []
    open_nodes = []
    open_nodes.append(start_node)
    visited.append(start_node.id)

    while len(open_nodes) > 0:
        open_nodes.sort(key = lambda x: x.fValue)
        current_node = open_nodes.pop(0)
        visited.append(current_node.id)
        neighbors = []

        if (current_node.id == goal_node.id):
            current_node.parents.append(current_node.id)
            return current_node.parents, current_node.getUCSDistance()
        
        for i in range(len(adj_m[0])):
            if (adj_m[current_node.id][i] != 0 and (i not in visited)):
                neighbors.append(i)

        for i in range(len(neighbors)):
            newFval = fVal(adj_m, current_node, neighbors[i])
            newNode = Node(neighbors[i], newFval)
            newNode.setParent(current_node)
            open_nodes.append(newNode)
    return None,None

if __name__ == "__main__":
    adj_m = [[0,75,0,140,0,0,0,0,118,0,0,0,0],
             [75,0,71,0,0,0,0,0,0,0,0,0,0],
             [0,71,0,151,0,0,0,0,0,0,0,0,0],
             [140,0,151,0,99,0,80,0,0,0,0,0,0],
             [0,0,0,99,0,211,0,0,0,0,0,0,0],
             [0,0,0,0,211,0,0,101,0,0,0,0,0],
             [0,0,0,80,0,0,0,97,0,0,0,120,146],
             [0,0,0,0,0,101,97,0,0,0,0,0,138],
             [118,0,0,0,0,0,0,0,0,111,0,0,0],
             [0,0,0,0,0,0,0,0,111,0,70,0,0],
             [0,0,0,0,0,0,0,0,0,70,0,75,0],
             [0,0,0,0,0,0,120,0,0,0,75,0,0],
             [0,0,0,0,0,0,146,138,0,0,0,0,0]]
    path,distance = ucs(adj_m,0,5)
    print(path,distance)