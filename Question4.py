from Question3 import addnode, graphvizcode,  pygraph
import random


def isConnected(g, s=None):
    """
    Checks if all the nodes of a given graph are connected
    :param g: graph - dictionary[item] = [connections]
    :param s: Starting node to check from
    :return: "Yes" or "No"
    """
    # If not starting node is given a random one is chosen
    if s is None:
        s = random.choice(list(g.keys()))
    found = [s]

    def connections(c):
        nonlocal found
        for connection in g[c]:
            if connection in found:
                continue
            else:
                found.append(connection)
                connections(connection)
    connections(s)
    if len(found) == len(g):
        return "Yes"
    else:
        return "No"


def graphvizconnectioncode(g):
    """
    Creates a Directed graph using GraphViz
    If the graph is connected then there will be an arrow to and from each connection
    :param g: graph - dictionary[item] = [connections]
    :return: None
    """
    found = []
    print("digraph {", end="")
    for node in g:
        for connection in g[node]:
            print(str(node) + " -> " + str(connection) + ";", end="")
            found.append([[connection], [node]])
    print("}")


if __name__ == "__main__":
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

    print(isConnected(g))

    graphvizcode(g)
    graphvizconnectioncode(g)
    # pygraph(g)
