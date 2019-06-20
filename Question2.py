from Question1 import readwords, tree_find, printinorder, gendot


class Node(object):
    """
    Class creates a node with a value and connections left and right.
    Modified from Question to include the nodes parent
    """

    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def tree_insert(item, tree=None):
    """
    Modified from Question 1 to include the parent tree
    item - String
    tree - object
    If tree is None a new tree is created
    Inserts 'item' in the tree 'tree'

    returns tree
    """
    if tree is None:
        tree = Node(item)

    else:
        if item < tree.value:
            if tree.left is None:
                tree.left = Node(item, tree)
            else:
                tree_insert(item, tree.left)
        else:
            if tree.right is None:
                tree.right = Node(item, tree)
            else:
                tree_insert(item, tree.right)
    return tree


def createtree(itemlist=None):
    """
    itemlist - list
    t - tree - object

    returns tree
    """
    if itemlist is None:
        return False
    for i in range(0, len(itemlist)):
        if i == 0:
            t = tree_insert(itemlist[i])
        else:
            tree_insert(itemlist[i], t)

    return t


def delete_node(node):
    """
    Deletes the given node from a tree
    :param node: tree defined by class Node
    :return: Bool if it deleted the node
    """

    # if the node as two children
    if node.left is not None and node.right is not None:
        # Takes the smallest item from the right sub-tree
        # Swaps the value, then deletes that node
        minnode = find_min_node(node.right)

        node.value = minnode.value

        delete_node(minnode)

        return True
    # if the node has no children
    if node.left is None and node.right is None:
        # Sets the parent.left or parent.right to None, depending on what side the node is on
        try:
            if node.parent.left.value == node.value:
                node.parent.left = None
        except AttributeError:
            pass

        try:
            if node.parent.right.value == node.value:
                node.parent.right = None
        except AttributeError:
            pass

        return True

    # if the node only has one child to the left
    if node.left is not None:
        try:
            if node.parent.left.value == node.value:
                node.parent.left = node.left
        except AttributeError:
            pass

        try:
            if node.parent.right.value == node.value:
                node.parent.right = node.left
        except AttributeError:
            pass

        return True

    # if the node only has one child to the right
    if node.right is not None:
        try:
            if node.parent.left.value == node.value:
                node.parent.left = node.right
        except AttributeError:
            pass

        try:
            if node.parent.right.value == node.value:
                node.parent.right = node.right
        except AttributeError:
            pass

        return True

    return False


def find_min_node(node):
    """
    Find the smallest item in a tree
    :param node: tree defined by class Node
    :return: node
    """
    # if there is a node to the left, go left else return the node
    if node.left is None:
        return node

    return find_min_node(node.left)


if __name__ == "__main__":
    words = readwords("Words.txt")
    bintree = createtree(words)
    nodetodelete = tree_find("box", bintree, False)
    if nodetodelete is False:
        print("Word not found")
    else:
        print("In order before deletion \n", printinorder(bintree))
        delete_node(nodetodelete)
        print("In order after deleting the word box \n", printinorder(bintree))
