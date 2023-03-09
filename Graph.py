class Node:
    def __init__(self, name, domain, adjacentList, color):
        self.name = name
        self.domain = domain
        self.adjacentList = adjacentList
        self.color = color

    # overloading the == operator:
    def __eq__(self, otherNode):
        return(self.color == otherNode.color)

    def addAdjacent(self, adjacentNode):
        if adjacentNode not in self.adjacentList:
            self.adjacentList.append(adjacentNode)
            adjacentNode.adjacentList.append(self)




