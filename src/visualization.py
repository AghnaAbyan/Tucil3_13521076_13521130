import networkx as nx
import matplotlib.pyplot as plt

def adj_mToEdges(adj_m,nodes):
    edges = []
    for i in range(len(adj_m)):
        for j in range(len(adj_m)):
            if (adj_m[i][j] != 0 and i<j):
                edges.append((nodes[i][0],nodes[j][0]))
    return edges

def getWeight(adj_m,nodes_name,edge):
    for x in range(len(nodes_name)):
        if (nodes_name[x][0] == edge[0]):
            i = x
        if (nodes_name[x][0] == edge[1]):
            j = x
    return adj_m[i][j]

def isPath(edge,path,nodes_name):
    pathEdges1 = []
    pathEdges2 = []
    for i in range(len(path)-1):
        pathEdges1.append((nodes_name[path[i]][0],nodes_name[path[i+1]][0]))
        pathEdges2.append((nodes_name[path[i+1]][0],nodes_name[path[i]][0]))
    if (edge in pathEdges1 or edge in pathEdges2):
            return True
    return False

def drawgraph(nodes,adj_m,path):
    G = nx.Graph()
    for i in range(len(nodes)):
        G.add_node(nodes[i][0],pos=(nodes[i][2],nodes[i][1]))
    edges = adj_mToEdges(adj_m,nodes)
    for i in range(len(edges)):
        c = '#93B8C5'
        if (isPath(edges[i],path,nodes)):
            c = 'r'
        G.add_edge(edges[i][0],edges[i][1],weight=round(getWeight(adj_m,nodes,edges[i]),2),color=c)

    pos = nx.get_node_attributes(G,'pos')
    labels = nx.get_edge_attributes(G,'weight')
    edges,colors = zip(*nx.get_edge_attributes(G, 'color').items())
    nx.draw_networkx(G,pos)
    nx.draw_networkx_edges(G,pos,edgelist=edges,edge_color=colors)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    adj_m = [[0,1,0,0,0,10,0],
         [1,0,2,1,0,0,0],
         [0,2,0,0,5,0,0],
         [0,1,0,0,3,4,0],
         [0,0,5,3,0,2,0],
         [10,0,0,4,2,0,5],
         [0,0,0,0,5,0,0]]
    nodes = [["bonbin",0,1],["kota",1,5],["kabupaten",2,7],["provinsi",3,8],["negara",4,9],["benua",5,5],["planet",8,-1]]
    path = [0,1]
    drawgraph(nodes,adj_m,path)