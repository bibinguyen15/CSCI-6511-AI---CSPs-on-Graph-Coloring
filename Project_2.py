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


def main():
    data = readFile("TestCases\\test0.txt")
    result = graphColoring(data)


def graphColoring(data):
    colors, edges = data
    print(colors, edges)


if __name__ == '__main__':
    main()


vertices = [1, 2, 3, 4, 5]
graph = {}
# Type dictionary with each color mapped to a list of list
#list[0] is color, list[1] is neighbors,
graph[1] = [[0], [2, 3, 5], [1, 2, 3]]
