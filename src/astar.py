from graph import *

def getFvalue(adj_m, heuristik, parent_node, node):
    g = parent_node[1] - heuristik[parent_node[0]] + adj_m[parent_node[0]][node]
    h = heuristik[node]
    return g+h

def astar(adj_m,heuristik,start_node,goal_node):

    visited = []
    open_nodes = []
    open_nodes.append([start_node,heuristik[start_node]])

    # parent dictionary
    parent = {}
    for i in range(len(adj_m[0])):
        parent[i] = None
    print(parent)

    while len(open_nodes) > 0 :
        # sort open nodes by f values (g+h)
        open_nodes.sort(key=lambda x: x[1])
        current_node = open_nodes.pop(0)
        visited.append(current_node[0])

        if current_node[0]==goal_node:
            path = []
            while current_node[0] != start_node:
                path.append(current_node[0])
                current_node[0] = parent[current_node[0]]
            path.append(start_node)
            return path[::-1]

        neighbor = []
        for i in range(len(adj_m[0])):
            if (adj_m[current_node[0]][i]!=0 and (i not in visited)):
                neighbor.append(i)

        for i in range(len(neighbor)):
            parent[neighbor[i]] = current_node[0]
            open_nodes.append([neighbor[i],getFvalue(adj_m,heuristik,current_node,neighbor[i])])

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