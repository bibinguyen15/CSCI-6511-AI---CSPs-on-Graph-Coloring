class GraphColoring:
    def __init__(self, nodes, colors):
        self.nodes = nodes
        self.colors = colors
        self.visited = []

    def get_ans(self):
        answer = {}
        for node in list(self.nodes.keys()):
            answer[node] = self.nodes[node]['color']
        print(answer)

    # will be arc consistency later
    def update_domains(self, node, color):
        neighbors_changed = []

        for neighbor in self.nodes[node]['neighbors']:
            if neighbor not in self.visited:
                if color in self.nodes[neighbor]['domain']:
                    self.nodes[neighbor]['domain'].remove(color)
                    neighbors_changed.append([neighbor, color])
        return neighbors_changed

    def consistent(self, node, color):
        for neighbor in self.nodes[node]['neighbors']:
            if neighbor in self.visited:
                if color == self.nodes[neighbor]['color']:
                    return False
        return True

    def solve(self, i):
        if(i == len(self.nodes)):
            self.get_ans()
            return True

        selected = self.get_node()

        ordered_colors = self.order_colors(selected)

        for color in ordered_colors:
            if self.consistent(selected, color):

                self.nodes[selected]['color'] = color

                neighbors = self.update_domain(selected, color)

                self.visited.append(selected)

                if self.solve(i + 1):
                    return True

                self.nodes[selected]['color'] = 0
                self.nodes[selected]['domain'] = ordered_colors
                self.visited.remove(selected)

                for neighbor in neighbors:
                    self.node[neighbor[0]]['domain'].append(neighbor[1])

        return False

    def get_node(self):
        dx = dict()
        # Get the node with the smallest domain that are not visited
        for item in self.nodes:
            if item not in self.visited:
                dx[item] = (len(self.nodes[item]['domain']),
                            self.nodes[item]['neighbor'])

        min_domain = min(list(dx.values())[0])

        max_neighbor = {}
        selected = ''
        # finding the node that has the most neighbors
        for key in dx.keys():
            if dx[key][0] == min_domain:
                neighbor = dx[key][1]
                if(len(neighbor) > len(max_neighbor)):
                    max_neighbor = neighbor
                    selected = key

        return selected

    def order_colors(self, node):
        return self.nodes[node]['domain']
