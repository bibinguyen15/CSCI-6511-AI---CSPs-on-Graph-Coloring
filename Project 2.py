def readFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        edges = []
        colors = int(data[2][9:10])

        for line in data[4:]:
            edge = line[0:-1]
            edges.append((int(edge[0]), int(edge[-1])))
        return colors, edges


def main():
    colors, edges = readFile("test0.txt")
    print(colors, edges)

    for edge in edges:
        print()


main()


