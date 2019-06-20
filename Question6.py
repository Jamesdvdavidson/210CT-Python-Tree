

def addnode(g, item, connections=None):
    """
    Adds a node to a graph
    :param g: graph - dictionary[item] = [connections]
    :param item: integer - item to be added
    :param connections: list/integer - connections from item to be added
    :return: new graph
    """
    g[item] = []
    # if there are no connections
    if connections is []:
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




if __name__ == "__main__":

    # g: graph - dictionary[item] = [[connection],[weight]]

    g = {}

    g = addnode(g, 0, [[1, 4], [7, 8]])
    g = addnode(g, 1, [[0, 4], [2, 8], [7, 11]])
    g = addnode(g, 2, [[1, 8], [3, 7], [5, 4], [8, 2]])
    g = addnode(g, 3, [[2, 7], [4, 9], [5, 14]])
    g = addnode(g, 4, [[3, 9], [5, 10]])
    g = addnode(g, 5, [[2, 4], [3, 14], [4, 10], [6, 2]])
    g = addnode(g, 6, [[5, 2], [7, 1], [8, 6]])
    g = addnode(g, 7, [[0, 8], [1, 11], [6, 1], [8, 7]])
    g = addnode(g, 8, [[2, 2], [6, 6], [7, 7]])

    print(g)

    print(dijsktra(g, 0))
