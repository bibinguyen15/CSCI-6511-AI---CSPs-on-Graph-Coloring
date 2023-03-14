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
# var is going to be the index of the variable last assigned in graph


def backTrack(oGraph, var):
    # if assign is a complete assignment
    # Look at leaf, update current best
    # return
    if not oGraph.notDone():
        return oGraph.getMap()

    # Choose unassigned variable Xi
    # Right now just choosing the next in graph
    var += 1

    # Order values v in domain i of Xi, least constraining values need to be implemented

    graph = Graph()
    best_assignment = {}

    # For each value v in that order:
    for v in oGraph.domains[var]:
        if(var == 0):
            print("\n_____Assigning first node color:", v, "\n")
        graph.copy(oGraph)

        node = graph.graph[var]
        #print("Assigning node", node.name, "color", v)
        node.color = v
        # Check constraints
        delta = checkConstraints(node, graph)
        if not delta:
            print("Constraints violated")
            continue

        # Arc Consistency

        # Check if any domain from any node is empty
        if arcConsistency(node, graph):
            print("Dead-end leaf")
            continue

        print(graph.getMap())
        assignment = backTrack(graph, var)
        if assignment:
            # Found a valid assignment
            if not best_assignment or len(assignment) < len(best_assignment):
                best_assignment = assignment

    return best_assignment

# def backTrack(oGraph, var):
    # if assign is a complete assignment
    # Look at leaf, update current best
    # return
    # if not oGraph.notDone():
    # return oGraph.getMap()

    # Choose unassigned variable Xi
    # Right now just choosing the next in graph
    #var += 1

    # Order values v in domain i of Xi, least constraining values need to be implemented

    #graph = Graph()
    # For each value v in that order:
    # for v in oGraph.domains[var]:
    # print("Running")
    # graph.copy(oGraph)

    #node = graph.graph[var]
    #print("Assigning node", node.name, "color", v)
    #node.color = v
    # Check constraints
    #delta = checkConstraints(node, graph)
    # if not delta:
    #print("Constraints violated")
    # continue

    # Arc Consistency

    # Check if any domain from any node is empty
    # if arcConsistency(node, graph):
    #print("Dead-end leaf")
    # continue
    # print(graph.getMap())
    # return backTrack(graph, var)

    # return {}


def checkConstraints(node, graph):
    for adjacent in node.adjacentList:
        if graph.getNode(adjacent).color == node.color:
            return False
    return True


def arcConsistency(node, graph):
    # for now will only do forward looking
    for adjacent in node.adjacentList:
        neighbor = graph.getNode(adjacent)
        if node.color in neighbor.domain:
            neighbor.domain.remove(node.color)
        if neighbor.domain == []:
            return True


main()
