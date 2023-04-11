class Node:
    def __init__(self,id,fValue):
        self.id = id
        self.fValue = fValue
        self.parents = []
    
    def setParent(self,parent_node):
        for i in parent_node.getParents():
            self.parents.append(i)
        self.parents.append(parent_node.getId())