from Graph import Node
from Graph import *
import random
import copy


def readFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        edges = []
        colors = int(data[2][9:10])

        for line in data[4:]:
            if line[-1] == "\n":
                line = line[0:-1]
            edges.append(line.split(","))

        print("---Problem:", colors, "- Edges:", edges)
        return colors, edges


def makeGraph(graph, colors, edges):
    for edge in edges:
        if edge[0] not in graph:
            a = Node(edge[0], [i for i in range(1, colors + 1)])
            graph.addNode(a)
        else:
            a = graph.getNode(edge[0])

        if edge[1] not in graph:
            b = Node(edge[1], [i for i in range(1, colors + 1)])
            graph.addNode(b)
        else:
            b = graph.getNode(edge[1])

        a.addAdjacent(b)

    # sort by the most to the least neighbors
    # Most Constrained Variable
    graph.sort()
    for node in graph.graph:
        graph.domains.append(node.domain)
    print(graph.getMap())

    graph.printGraph()
    print(graph.domains)


def main():
    colors, edges = readFile("TestCases\\test3.txt")
    graph = Graph()

    makeGraph(graph, colors, edges)
    print(backTrack(graph, -1))
    edge1 = [1, 2, 3]
    edge2 = [2, 3]
    print(edge1 + edge2)


main()
