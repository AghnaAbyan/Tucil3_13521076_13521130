from astar import astar
from filereader import getLines,fileReader
import visualisation as vis

def printNodesName(path,lines):
    n = (len(lines)-1)//2
    nodes_name = [el[0] for el in [[x for x in line.split(' ')] for line in lines][1:n+1]]
    for i in range(len(path)):
        print(str(i+1) + ". "+ nodes_name[path[i]])
    print()
    return nodes_name

# welcome message
print("Welcome to Path Finder\n")

while (True):
    # home
    print("Please choose an option:")
    print("1. Run Path Finder\n2. Exit")
    while (True):
        option = int(input(">> "))
        print()
        if (option==1 or option==2):
            break
        else:
            print("Invalid option, please try again\n")
    if (option==2):
        break

    # choose file
    print("Enter file name:")
    while (True):
        fileName = input(">> ")
        print()
        try:
            lines = getLines("test/"+fileName)
            break
        except:
            print("File not found, please try again\n")

    # choose distance method
    print("Please choose the distance method calculation:")
    print("1. Euclidean\n2. Haversine")
    while (True):
        distance_method = int(input(">> "))
        print()
        if (distance_method==1 or distance_method==2):
            break
        else:
            print("Invalid option, please try again\n")

    # choose path finder method
    print("Please choose path finder method:")
    print("1. UCS\n2. A*")
    while (True):
        path_finder_method = int(input(">> "))
        print()
        if (path_finder_method==1 or path_finder_method==2):
            break
        else:
            print("Invalid option, please try again\n")

    # choose start node
    p = [i for i in range((len(lines)-1)//2)]
    printNodesName(p,lines)
    print("Please choose the start node:")
    while (True):
        start_node = int(input(">> "))-1
        print()
        if (start_node >= 0 and start_node < int(lines[0])):
            break
        else:
            print("Invalid start node, please try again\n")

    # choose goal node
    print("Please choose the goal node:")
    while (True):
        goal_node = int(input(">> "))-1
        print()
        if (goal_node >= 0 and goal_node < int(lines[0])):
            break
        else:
            print("Invalid goal node, please try again\n")

    # path finding
    if (path_finder_method == '1'):
        adj_m,nodes = fileReader(lines,start_node,goal_node,distance_method,path_finder_method)
        print(adj_m,"\n")
    else:
        adj_m,heuristik,nodes = fileReader(lines,start_node,goal_node,distance_method,path_finder_method)
        path,distance = astar(adj_m,heuristik,start_node,goal_node)
        if (path==None):
            print("")
        print("Result: ")
        printNodesName(path,lines)
        print("Distance:",round(distance,2),"km\n")

    # visualisation
    print("Do you want to visualise the graph? (y/n)")
    while (True):
        visualisation = input(">> ")
        print()
        if (visualisation=='y' or visualisation=='n'):
            break
        else:
            print("Invalid option, please try again\n")
    if (visualisation=='y'):
        print("Exit visualisation to continue\n")
        vis.drawgraph(nodes,adj_m,path)