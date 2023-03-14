import copy


class Node:
    def __init__(self, name="", domain=[]):
        self.name = name
        self.domain = domain
        self.adjacentList = []
        self.color = 0

    # overloading the == operator:
    def __eq__(self, otherNode):
        return self.name == otherNode.name

    def addAdjacent(self, adjacentNode):
        if adjacentNode.name not in self.adjacentList:
            self.adjacentList.append(adjacentNode.name)
            adjacentNode.adjacentList.append(self.name)

    def print(self):
        print("Node:", self.name, "- Domain:", self.domain,
              "- Neighbors:", [node for node in self.adjacentList],
              "- Color assigned:", self.color)

    def copy(self, otherNode):
        self.name = otherNode.name
        self.domain = copy.deepcopy(otherNode.domain)
        self.adjacentList = copy.deepcopy(otherNode.adjacentList)
        self.color = otherNode.color
        #print("Finished copying node", self.name)
        return self


class Graph:
    def __init__(self, graph=[], domains=[]):
        self.graph = graph
        self.domains = domains
        print("Initializing new graph.")

    def __eq__(self, otherGraph):
        return self.graph == otherGraph.graph

    def __contains__(self, name):
        return any(node.name == name for node in self.graph)
        # return node.name in self.graph

    def addNode(self, node):
        self.graph.append(node)
        self.domains.append(node.domain)

    # sorts list of variables in order of decreasing constraints
    def sort(self):
        self.graph.sort(key=lambda node: len(
            node.adjacentList), reverse=True)

    def getNode(self, name):
        for node in self.graph:
            if node.name == name:
                return node

    def getMap(self):
        colorMap = {}
        for node in self.graph:
            colorMap[node.name] = node.color
        return colorMap

    def printGraph(self):
        print("-------------------------------")
        for node in self.graph:
            node.print()
        print("-------------------------------")

    def copy(self, otherGraph):
        #print("Started copying graph")
        graph = []
        for node in otherGraph.graph:
            a = Node()
            graph.append(a.copy(node))
        self.graph = graph
        self.domains = copy.deepcopy(otherGraph.domains)
        #print("finished copying graph")
        return self

    def notDone(self):
        return any(node.color == 0 for node in self.graph)


