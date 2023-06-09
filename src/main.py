from astar import astar
from ucs import ucs
from filereader import getLines,fileReader
import visualization as vis
from flask import Flask, render_template
import googlemaps
from colorama import Fore, Style

def printNodesName(path,lines):
    n = (len(lines)-1)//2
    nodes_name = [el[0] for el in [[x for x in line.split(' ')] for line in lines][1:n+1]]
    for i in range(len(path)):
        print(str(i+1) + ". "+ nodes_name[path[i]])
    print()


# welcome message
print("Welcome to: \n")
print(Fore.YELLOW + "     ___     ___     _____    _  _                 ___     ___     _  _      ___      ___      ___    ")
print("    | _ \   /   \   |_   _|  | || |      o O O    | __|   |_ _|   | \| |    |   \    | __|    | _ \   ")
print("    |  _/   | - |     | |    | __ |     o         | _|     | |    | .` |    | |) |   | _|     |   /   ")
print("   _|_|_    |_|_|    _|_|_   |_||_|    TS__[O]   _|_|_    |___|   |_|\_|    |___/    |___|    |_|_\   ")
print(Fore.BLUE + ' _| """ | _|"""""| _|"""""| _|"""""|  {======| _| """ | _|"""""| _|"""""| _|"""""| _|"""""| _|"""""|  ')
print(Fore.BLACK + " ''-0-0-' ''-0-0-' ''-0-0-' ''-0-0-' ./o--000' ''-0-0-' ''-0-0-' ''-0-0-' ''-0-0-' ''-0-0-' ''-0-0-'  ")
print(Fore.WHITE + "                                    Created by " + Fore.GREEN + "ABYAN" + Fore.WHITE + " and " + Fore.MAGENTA + "ALTHAA")
print(Style.RESET_ALL)

while (True):
    # home
    print("Please choose an option:")
    print("1. Run Path Finder\n2. Exit")
    while (True):
        option = input(">> ")
        print()
        if (option=='1' or option=='2'):
            option = int(option)
            break
        else:
            print("Invalid option, please try again\n")
    if (option==2):
        print(Fore.CYAN + "               ___       ___                            ___          ")
        print("              (   )     (   )                          (   )         ")
        print("               | |_      | | .-.     .---.   ___ .-.    | |   ___    ")
        print("              (   __)    | |/   \   / .-, \ (   )   \   | |  (   )   ")
        print("               | |       |  .-. .  (__) ; |  |  .-. .   | |  ' /     ")
        print("               | | ___   | |  | |    .'`  |  | |  | |   | |,' /      ")
        print("               | |(   )  | |  | |   / .'| |  | |  | |   | .  '.      ")
        print("               | | | |   | |  | |  | /  | |  | |  | |   | | `. \     ")
        print("               | ' | |   | |  | |  ; |  ; |  | |  | |   | |   \ \    ")
        print("               ' `-' ;   | |  | |  ' `-'  |  | |  | |   | |    \ .   ")
        print("                `.__.   (___)(___) `.__.'_. (___)(___) (___ ) (___)  ")                               
        print("                           ___  ___    .--.    ___  ___   ")
        print("                          (   )(   )  /    \  (   )(   )  ")
        print("                           | |  | |  |  .-. ;  | |  | |   ")
        print("                           | |  | |  | |  | |  | |  | |   ")
        print("                           | '  | |  | |  | |  | |  | |   ")
        print("                           '  `-' |  | |  | |  | |  | |   ")
        print("                            `.__. |  | '  | |  | |  ; '   ")
        print("                            ___ | |  '  `-' /  ' `-'  /   ")
        print("                           (   )' |   `.__.'    '.__.'    ")
        print("                            ; `-' '                       ")
        print("                             .__.'                        \n")
        print(Style.RESET_ALL)
        break

    # choose file
    print("Enter file name:")
    while (True):
        fileName = input(">> ")
        print()
        try:
            lines = getLines("../test/"+fileName)
            break
        except:
            print("File not found, please try again\n")

    # choose distance method
    print("Please choose the distance method calculation:")
    print("1. Euclidean, use this if your nodes position is in cartesian coordinate")
    print("2. Haversine, use this if your nodes position is in latitude and longitude")
    while (True):
        distance_method = input(">> ")
        print()
        if (distance_method=='1' or distance_method=='2'):
            distance_method = int(distance_method)
            break
        else:
            print("Invalid option, please try again\n")

    # choose path finder method
    print("Please choose the path finder method:")
    print("1. UCS\n2. A*")
    while (True):
        path_finder_method = input(">> ")
        print()
        if (path_finder_method=='1' or path_finder_method=='2'):
            path_finder_method = int(path_finder_method)
            break
        else:
            print("Invalid option, please try again\n")

    # choose start node
    print("The nodes are as follows:")
    p = [i for i in range((len(lines)-1)//2)]
    printNodesName(p,lines)
    print("Please choose the start node:")
    while (True):
        start_node = input(">> ")
        print()
        if (int(start_node)-1 >= 0 and int(start_node)-1 < int(lines[0])):
            start_node = int(start_node)-1
            break
        else:
            print("Invalid start node, please try again\n")

    # choose goal node
    print("Please choose the goal node:")
    while (True):
        goal_node = input(">> ")
        print()
        if (int(goal_node)-1 >= 0 and int(goal_node)-1 < int(lines[0])):
            goal_node = int(goal_node)-1
            break
        else:
            print("Invalid goal node, please try again\n")

    # path finding
    isFound = True
    if (path_finder_method == 1):
        adj_m,nodes = fileReader(lines,goal_node,distance_method,path_finder_method)
        path,distance = ucs(adj_m,start_node,goal_node)
        if (path==None):
            print("No path found, please make sure that both start node and goal node are connected\n")
            isFound = False
        else:
            if (distance_method==1): unit = "unit"
            else: unit = "km"
            print("Result: ")
            printNodesName(path,lines)
            print("Distance:",round(distance,2),"%s\n"%(unit))
    else:
        adj_m,heuristik,nodes = fileReader(lines,goal_node,distance_method,path_finder_method)
        path,distance = astar(adj_m,heuristik,start_node,goal_node)
        if (path==None):
            print("No path found, please make sure that both start node and goal node are connected\n")
            isFound = False
        else:
            if (distance_method==1): unit = "unit"
            else: unit = "km"
            print("Result: ")
            printNodesName(path,lines)
            print("Distance:",round(distance,2),"%s\n"%(unit))

    # visualization
    if(isFound):
        print("How do you want to visualize the path?")
        print("1. Graph\n2. Map\n3. No visualization")
        while (True):
            visualization = input(">> ")
            print()
            if (visualization=='1' or visualization=='2' or visualization<='3'):
                visualization = int(visualization)
                break
            else:
                print("Invalid option, please try again\n")

        if (visualization==1 or visualization==2):
            print("Exit visualization to continue\n") 
            if (visualization==1):
                vis.drawgraph(nodes,adj_m,path)
            else:
                path = [[nodes[path[i]][1],nodes[path[i]][2]] for i in range(len(path))]
                # print(nodes)
                app = Flask(__name__)
                @app.route('/')
                def map():
                    gmaps = googlemaps.Client(key='AIzaSyBysSbgLtum7i-eQ3_qMqiMMsVlNHe88Yw')
                    return render_template('map.html',gmaps=gmaps,nodes=nodes,path=path)
                app.run(debug=False)