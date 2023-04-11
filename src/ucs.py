class Node:
    def __init__(self,id,fValue):
        self.id = id
        self.fValue = fValue
        self.parents = []
    
    def setParent(self,parent_node):
        for i in parent_node.parents:
            self.parents.append(i)
        self.parents.append(parent_node.id)

    def print(self):
        print(self.id,", ",self.fValue,", ",self.parents)

    def getDistance(self):
        return self.fValue

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
            return current_node.parents, current_node.getDistance()
        
        for i in range(len(adj_m[0])):
            if (adj_m[current_node.id][i] != 0 and (i not in visited)):
                neighbors.append(i)

        for i in range(len(neighbors)):
            newFval = fVal(adj_m, current_node, neighbors[i])
            newNode = Node(neighbors[i], newFval)
            newNode.setParent(current_node)
            open_nodes.append(newNode)

    return None

adj_m = [[0,2,0,5,0,0,0],
         [0,0,0,0,0,0,1],
         [0,4,0,0,0,0,0],
         [0,0,0,0,2,0,6],
         [0,0,4,0,0,3,0],
         [0,0,6,0,0,0,3],
         [0,0,0,0,7,0,0]]

path, distance = ucs(adj_m,0,6)
print("Path: ", path)
print("Distance: ", distance)