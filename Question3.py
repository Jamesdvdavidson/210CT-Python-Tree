from graphviz import Graph


def addnode(g, item, connections=None):
    """
    Adds a node to a graph
    :param g: graph - dictionary[item] = [connections]
    :param item: integer - item to be added
    :param connections: list/integer - connections from item to be added
    :return: new graph
    """
    g[item] = []
    # if only one connection is given as an integer
    if connections is int:
        connections = [connections]
    # if there are no connections
    if connections is [] or None:
        g[item] = None
        return g
    # adding connections
    if connections is not None:

        for i in range(0, len(connections)):
            if i == 0:
                g[item] = [connections[i]]
            else:
                g[item].append(connections[i])

    return g


def ispath(g, v1, v2, p=[], d=0):
    """
    Checks for a path from v1 to v2
    :param g: dictionary - Graph
    :param v1: integer - Start node
    :param v2: integer - destination node
    :param p: list - path
    :param d: integer - Stores the current depth of recursion
    :return: list - Path / None
    """
    d += 1
    p.append(v1)
    # If the destination node is found
    if v1 == v2:
        return p
    # else
    if v1 not in g:
        return None
    if v2 not in g:
        return None

    # loops for every node in the connections of the current node
    for connection in g[v1]:
        if connection not in p:
            # Goes to loop through all the connections of this node
            newpath = ispath(g, connection, v2, p, d)

            if newpath:
                if d == 1:
                    # print to file
                    with open("Path.txt", "a") as f:
                        f.write(str(p) + " Path for connecting " + str(v1) + " to " + str(v2) + "\n")
                return newpath
    if d == 0:
        print("No path found")
    return None


def graphvizcode(g):
    """
    Generates dot code for the given graph
    :param g: dictionary - graph
    :return: None
    """
    found = []
    print("graph {", end="")
    for node in g:
        for connection in g[node]:
            if not ([[node], [connection]] in found or [[connection], [node]] in found):
                print(str(node) + " -- " + str(connection) + ";", end="")
                found.append([[connection], [node]])
    print("}")


def pygraph(g):
    """
    Uses the python graphviz module to generate a given graph
    :param g: dictionary - graph
    :return: None
    """
    found = []
    dot = Graph()

    for nodes in g:
        dot.node(str(nodes))

    for node in g:
        for connection in g[node]:
            if not ([[node], [connection]] in found or [[connection], [node]] in found):
                dot.edge(str(connection), str(node))
                found.append([[connection], [node]])
    dot.render(view=True)


if __name__ == "__main__":
    """
    g = Dictionary key=item [Connections]
    item = +ve integer 
    """

    g = {}

    g = addnode(g, 0, [0, 1, 7])
    g = addnode(g, 1, [0, 2, 6])
    g = addnode(g, 2, [1, 3, 4, 9])
    g = addnode(g, 3, [2])
    g = addnode(g, 4, [2, 5])
    g = addnode(g, 5, [4])
    g = addnode(g, 6, [1, 7, 8])
    g = addnode(g, 7, [0, 6])
    g = addnode(g, 8, [6])
    g = addnode(g, 9, [2])

    for node in g:
        print(node, ": ", g[node])

    print(ispath(g, 3, 8))

    graphvizcode(g)
