import copy


def main():
    data = readFile("TestCases\\test6.txt")
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

    print(graph)

    csp = CSP(nodes, graph, colors)

    result = csp.solve()
    if result == None:
        print("No solutions")
    else:
        print(result)


class CSP:
    def __init__(self, nodes, graph, colors):
        self.nodes = nodes
        self.graph = graph
        self.colors = colors
        self.visited = []

    def printGraph(self):
        for node in self.nodes:
            print(node, ":", self.graph[node])

    def solve(self, assignment={}):
        if len(assignment) == len(self.nodes):
            return assignment

        selected = self.selectNode()

        orderedColors = self.orderColor(selected)
        print("Ordered colors is:", orderedColors)

        for color in orderedColors:
            if self.consistent(selected, color, assignment):
                # Make deep copy to return to original in leaf cases
                nGraph = copy.deepcopy(self.graph)

                # Assigning the color to the node
                assign = assignment.copy()
                assign[selected] = color
                self.graph[selected][0] = [color]
                print("Assigning", selected, "with", color)

                print(assign)

                # Add to visited
                self.visited.append(selected)

                if self.ac3(selected):
                    result = self.solve(assign)
                    if result is not None:
                        return result

                # Return all values back
                self.graph = nGraph
                self.visited.remove(selected)

        return None

    def ac3(self, selected):
        # For now only do simple forward checking
        for neighbor in self.graph[selected][1]:
            if neighbor not in self.visited:
                if self.graph[selected][0][0] in self.graph[neighbor][0]:
                    self.graph[neighbor][0].remove(
                        self.graph[selected][0][0])
                if not self.graph[neighbor][0]:
                    print(neighbor, "has empty domain")
                    return False

        self.printGraph()
        return True

    def consistent(self, selected, color, assignment):
        for neighbor in self.graph[selected][1]:
            if assignment.get(neighbor) == color:
                return False
        return True

    def selectNode(self):
        # Choose based on most constraints, first choose one with least domain
        minDomain = len(
            min([v[0] for k, v in self.graph.items() if k not in self.visited],
                key=len))
        mcv = [(k, v[1])
               for k, v in self.graph.items() if len(v[0]) == minDomain and k not in self.visited]

        mcv.sort(key=lambda elem: len(elem[1]), reverse=True)
        print("Selected node is:", mcv[0][0], "from", mcv)
        return mcv[0][0]

    def orderColor(self, node):
        colors = []
        for color in self.graph[node][0]:
            consistent = 0
            for neighbor in self.graph[node][1]:
                consistent += len([i for i in self.graph[neighbor]
                                  [0] if i != color])
            colors.append((color, consistent))

        # want to sort based on highest consistency ratings
        colors.sort(key=lambda elem: elem[1], reverse=True)

        return [i[0] for i in colors]


'''
    
    
    
    
    
    
    
    
    
    
    
'''
if __name__ == '__main__':
    main()


