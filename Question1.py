import re
from pathlib import Path


class Node(object):
    """ Class creates a node with a value and connections left and right """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_insert(item, tree=None):
    """
    item - String
    tree - object
    If tree is None a new tree is created
    Inserts 'item' in the tree 'tree'

    returns tree
    """

    item = item.lower()

    if tree is None:
        tree = Node(item)

    else:
        if item < tree.value:
            if tree.left is None:
                tree.left = Node(item)
            else:
                tree_insert(item, tree.left)
        else:
            if tree.right is None:
                tree.right = Node(item)
            else:
                tree_insert(item, tree.right)
    return tree


def tree_find(item, tree=None, verbose=True):
    """
    item - String
    tree - object

    Finds 'item' in tree 'tree'

    returns Whether it found the 'item'
    """

    item = item.lower()

    if tree.value is None:
        print("No tree given")
        return False
    found = "No"

    def findrecurse(tree):
        """
        tree - object

        recursive calls to find item in tree

        returns "Yes" or "No"
        """
        if tree.value == item:
            if verbose:
                print("Item found")
            nonlocal found
            found = "Yes"
            return tree
        elif tree.value > item:
            if verbose:
                print(item + " is less than '" + tree.value + "' Going left")
            if tree.left is None:
                return False
            else:
                return findrecurse(tree.left)
        elif tree.value < item:
            if verbose:
                print(item + " is more than '" + tree.value + "' Going right")
            if tree.right is None:
                return False
            else:
                return findrecurse(tree.right)
        return False

    node = findrecurse(tree)

    if found == "No":
        if verbose:
            print("'" + item + "' was not found in the tree!")
        return False
    return node


def tree_count(tree):
    """
    tree - object
    data - list
    count - dictionary

    returns count
    """
    data = printinorder(tree)
    count = {}

    def countrecurse(word):
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    for word in data:
        # Loops through all words in data
        countrecurse(word)
    return count


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


def printpreorder(tree):
    """
    tree - object
    data - list

    returns data - in pre order
    """
    data = []

    def prerecurse(node):
        if not node:
            return
        data.append(node.value)
        prerecurse(node.left)
        prerecurse(node.right)

    prerecurse(tree)
    return data


def printpostorder(tree):
    """
    tree - object
    data - list

    returns data - in post order
    """
    data = []

    def postrecurse(node):
        if not node:
            return
        postrecurse(node.left)
        postrecurse(node.right)
        data.append(node.value)

    postrecurse(tree)
    return data


def printinorder(tree):
    """
    tree - object
    data - list

    returns data - in order
    """
    data = []

    def inrecurse(node):
        if not node:
            return
        inrecurse(node.left)
        data.append(node.value)
        inrecurse(node.right)

    inrecurse(tree)
    return data


def readwords(file):
    """
    Reads in a paragraph from Words.txt
    Then removes punctuation and splits it in to a list

    returns a list of words

    """
    if not Path(file).is_file():
        # If File is not found
        return None

    with open(file, "r") as f:
        inputwords = f.read()
        # Regex, Removes all non whitespace and non word characters, from the string inputwords
        inputwords = re.sub(r'[^\w\s]', '', inputwords)
        inputwords = inputwords.lower()

    wordslist = inputwords.split()

    # print(wordslist)
    return wordslist


def gendot(node):
    """
    Generates dot code used by GraphViz to generate visual representation of and tree given
    Software available here: https://graphviz.gitlab.io/
    Full tree generated 'Full_Tree.png'
    :param node: tree defined by class Node
    :return: dotttext - string
    """
    seq = 0

    def gencode(node, parentseq=None, lorr=None):
        """

        :param node: tree defined by class Node
        :param parentseq: integer - parent node for connections
        :param lorr: string - if the connections to parent was from the left or right
        :return: string - generated dot code
        """
        nonlocal seq
        seq += 1

        dot = ""
        # Creates the node
        dot += "node" + str(seq) + '[label="' + str(node.value) + '"];'

        if parentseq is not None:
            dot += "node" + str(parentseq) + ' -> ' + "node" + str(seq) + '[label="' + str(lorr) + '"];'

        thisseq = seq
        # Creates the connection
        if node.left is not None:
            dot += gencode(node.left, thisseq, "L")

        if node.right is not None:
            dot += gencode(node.right, thisseq, "R")

        return dot

    dottext = 'digraph { node [fixedsize=true, fontname="Arial", fontsize=8];'

    dottext += gencode(node)

    dottext += "}"

    return dottext


if __name__ == "__main__":
    words = readwords("Words.txt")
    bintree = createtree(words)
    print("Pre order ", printpreorder(bintree))
    print("Post order ", printpostorder(bintree))
    print("In order ", printinorder(bintree))
    print(tree_count(bintree))
    print(tree_find("word", bintree).value)
    print("\n" + str(gendot(bintree)))
