from GraphColoring import GraphColoring


def read_file(file):
    with open(file, 'r') as f:
        data = f.readlines()
        edges = []
        colors = int(data[2][9:10])

        for line in data[4:]:
            if line[-1] == "\n":
                line = line[0:-1]
            edges.append(line.split(","))

        print("---Problem:", colors, "- Edges:", edges)

        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = {'color': 0, 'neighbors': [edge[1]],
                                  'domain': [i for i in range(1, colors + 1)]}
            else:
                graph[edge[0]]['neighbors'] += [edge[1]]

            if edge[1] not in graph:
                graph[edge[1]] = {'color': 0, 'neighbors': [edge[0]],
                                  'domain': [i for i in range(1, colors + 1)]}
            else:
                graph[edge[1]]['neighbors'] += [edge[0]]
        print(graph)
        return colors, graph


def main():
    colors, graph = read_file("TestCases\\test0.txt")
    visited = []
    nodes = graph.keys()

    test = GraphColoring(nodes, colors)

    if not test.solve(0):
        print("Solution does not exist.")

    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # iterate over the keys and values in the dictionary
    for key in my_dict:
        value = my_dict[key]
        print(key, value)


main()
