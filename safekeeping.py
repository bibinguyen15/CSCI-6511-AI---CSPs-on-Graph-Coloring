

import copy


def main():
    data = readFile("TestCases\\test0.txt")
    result = graphColoring(data)


# Something to make space
# Call CSP to solve graph coloring
# csp = CSP(graph, nodes, colors)

# For testing purposed only


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
        return [colors, edges]


def graphColoring(data):
    colors, edges = data

    # Making the graph
    nodes = []
    graph = {}
    # processing each edges
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
            # value is color, domain, then neighbors
            graph[edge[0]] = [[i for i in range(1, colors + 1)], [edge[1]]]
        else:
            graph[edge[0]][1].append(edge[1])
        if edge[1] not in nodes:
            nodes.append(edge[1])
            graph[edge[1]] = [[i for i in range(1, colors + 1)], [edge[0]]]
        else:
            graph[edge[1]][1].append(edge[0])

    # graph['3'][1].append('2')
    for key in graph.keys():
        print(key, ":", graph[key])

    visited = []  # '3', '2', '19'

    print(max([v[1] for k, v in graph.items() if k not in visited], key=len))
    X = [k for k, v in graph.items() if len(v[1]) == 2 and k not in visited]

    print("Nodes in this graph:", nodes)

    minL = len(min([v[1] for k, v in graph.items()], key=len))
    Y = [(k, v[1]) for k, v in graph.items() if len(v[1]) == minL]

    print(Y)

    y = graph.copy()
    print(y)


if __name__ == '__main__':
    main()

















