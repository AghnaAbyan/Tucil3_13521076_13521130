class Node:
    def __init__(self,id,fValue):
        self.id = id
        self.fValue = fValue
        self.parents = []
    
    def setParent(self,parent_node):
        for i in parent_node.parents:
            self.parents.append(i)
        self.parents.append(parent_node.id)

def calculateFValue(adj_m, heuristik, parent_node, node):
    g = parent_node.fValue - heuristik[parent_node.id] + adj_m[parent_node.id][node]
    h = heuristik[node]
    return g+h

def astar(adj_m,heuristik,s_node,g_node):
    # initiate start_node and goal_node
    start_node = Node(s_node,heuristik[s_node])
    goal_node = Node(g_node,0)

    # visited, open_nodes
    visited = []
    open_nodes = []

    # visit start node
    open_nodes.append(start_node)
    visited.append(start_node.id)

    while len(open_nodes) > 0 :
        # sort open nodes by f values
        open_nodes.sort(key=lambda x: x.fValue)

        # visit open_nodes with smallest fValue
        current_node = open_nodes.pop(0)
        visited.append(current_node.id)

        # current node is goal node
        if current_node.id==goal_node.id:
            current_node.parents.append(current_node.id)
            return current_node.parents

        # find neighbors of current node
        neighbors = []
        for i in range(len(adj_m[0])):
            if (adj_m[current_node.id][i]!=0 and (i not in visited)):
                neighbors.append(i)

        # for each neighbors append to open nodes
        for i in range(len(neighbors)):
            newFvalue = calculateFValue(adj_m,heuristik,current_node,neighbors[i])
            newNode = Node(neighbors[i],newFvalue)
            newNode.setParent(current_node)
            open_nodes.append(newNode)

    return None

if __name__ == "__main__":
    adj_m = [[0,1,0,0,0,10],
             [1,0,2,1,0,0],
             [0,2,0,0,5,0],
             [0,1,0,0,3,4],
             [0,0,5,3,0,2],
             [10,0,0,4,2,0]]
    heuristik = [5,3,4,2,6,0]
    path = astar(adj_m,heuristik,0,5)
    print(path)