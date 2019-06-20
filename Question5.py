from Question3 import addnode


def dfs(g, v1, visit=None):
    """
    Depth first traversal of the graph
    :param g: graph - dictionary[item] = [connections]
    :param v1: integer - Where to start
    :param visit: list - where has been visited
    :return: visit
    """
    if visit is None:
        visit = []
    visit.append(v1)

    for next in g[v1]:
        if next in visit:
            continue
        else:
            dfs(g, next, visit)

    return visit


def dfstofile(g, v1):
    """
    Outputs dfs() to file dfs.txt
    :param g: graph - dictionary[item] = [connections]
    :param v1: integer - node to start from
    :return: the path found
    """
    output = dfs(g, v1)
    with open("dfs.txt", "a") as f:
        f.write(str(output) + " DFS starting at " + str(v1) + "\n")

    return output


def bfs(g, v1):
    """
    :param g: Graph - dictionary[key] = [connections]
    :param v1: Node to start from
    :return:
    """
    explored = []
    nodestocheck = [v1]
    # creates new dictionary
    depth = {v1: 0}

    visited = [v1]
    # While there are nodes left to check
    while nodestocheck:
        node = nodestocheck.pop(0)
        explored.append(node)
        connections = g[node]

        for connection in connections:
            if connection not in visited:
                nodestocheck.append(connection)
                visited.append(connection)

                depth[connection] = depth[node] + 1

    print(depth)

    with open("bfs.txt", "a") as f:
        f.write(str(list(depth.keys())) + " BFS starting at " + str(v1) + "\n")

    return list(depth.keys())


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

    print("DFS")
    print(dfstofile(g, 9))

    print("\nBFS")
    print(bfs(g, 5))
