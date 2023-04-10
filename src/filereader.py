from math import *

def getLines(fileName):
    file = open(fileName,'r')
    lines = []
    for line in file:
        line = line.rstrip()
        lines.append(line)
    return lines

def processNodes(lines):
    nNodes = int(lines[0])
    raw = []
    raw = [[x for x in line.split(' ')] for line in lines]
    nodes_raw = raw[1:nNodes+1]
    adj_m_raw = raw[nNodes+1:]
    return nodes_raw,adj_m_raw

def haversine(node1,node2):
    r = 6371
    dLat = pi/180 * (float(node1[1])-float(node2[1]))
    dLon = pi/180 * (float(node1[2])-float(node2[2]))
    akar =  sin(dLat/2)**2 + cos(float(node2[1])*(pi/180)) * cos(float(node1[1])*(pi/180)) * sin(dLon/2)**2
    return 2*r*asin(sqrt(akar))

def euclidean(node1,node2):
    d1 = (float(node1[1])-float(node2[1]))
    d2 = (float(node1[2])-float(node2[2]))
    return sqrt(d1**2+d2**2)

def getDistance(distance_method,node1,node2):
    if (distance_method==1):
        return euclidean(node1,node2)
    else:
        return haversine(node1,node2)

def getAdj_m(adj_m_raw,nodes_raw):
    n = len(adj_m_raw)
    adj_m = [[0 for i in range (n)] for j in range (n)]
    for i in range(n):
        for j in range(n):
            if(int(adj_m_raw[i][j])==1):
                adj_m[i][j] = haversine(nodes_raw[i],nodes_raw[j])
    return adj_m

def getHeuristik(adj_m_raw,nodes_raw,goal_node):
    heuristik = [0 for i in range(len(nodes_raw))]
    for i in range(len(nodes_raw)):
        heuristik[i] = haversine(nodes_raw[i],nodes_raw[goal_node])
    return heuristik            

def fileReader(lines,start_node,goal_node,distance_method,path_finder_method):
    nodes_raw,adj_m_raw = processNodes(lines)
    adj_m = getAdj_m(adj_m_raw,nodes_raw)
    if (path_finder_method==1):
        return adj_m
    else:
        return adj_m, getHeuristik(adj_m_raw,nodes_raw,goal_node)

if __name__ == "__main__":
    lines = getLines("test/testcase1.txt")
    nodes_raw,adj_m_raw = processNodes(lines)
    print(nodes_raw)
    print(adj_m_raw)
    print(getAdj_m(adj_m_raw,nodes_raw))
