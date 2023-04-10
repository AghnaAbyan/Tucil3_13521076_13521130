from astar import astar
from filereader import getLines,fileReader

def isOptionValid(option):
    if (option == '1' or option == '2'):
        return True
    else:
        return False

# welcome message
print("Welcome to Path Finder\n")

# choose file
print("Please choose the file you want to use:")
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
print("1. Euclidean\n2. Haversine\n")
while (True):
    distance_method = input(">> ")
    print()
    if (isOptionValid(distance_method)):
        break
    else:
        print("Invalid option, please try again\n")

# choose path finder method
print("Please choose path finder method:")
print("1. UCS\n2. A*\n")
while (True):
    path_finder_method = input(">> ")
    print()
    if (isOptionValid(path_finder_method)):
        break
    else:
        print("Invalid option, please try again\n")

# choose start node
print("Please choose the start node:")
while (True):
    start_node = int(input(">> "))
    print()
    if (start_node >= 0 and start_node < int(lines[0])):
        break
    else:
        print("Invalid start node, please try again\n")

# choose goal node
print("Please choose the goal node:")
while (True):
    goal_node = int(input(">> "))
    print()
    if (goal_node >= 0 and goal_node < int(lines[0])):
        break
    else:
        print("Invalid goal node, please try again\n")

# path finding
if (path_finder_method == '1'):
    adj_m = fileReader(lines,start_node,goal_node,distance_method,path_finder_method)
    print(adj_m)
else:
    adj_m,heuristik = fileReader(lines,start_node,goal_node,distance_method,path_finder_method)
    print(adj_m)
    print(heuristik)
    path  = astar(adj_m,heuristik,start_node,goal_node)
    print(path)