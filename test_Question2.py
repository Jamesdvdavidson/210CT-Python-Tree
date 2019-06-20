from unittest import TestCase


class Test_Question_2(TestCase):

    def test_find_min_node(self):
        # Finds the left most node from a subtree
        from Question2 import readwords, createtree, tree_find, find_min_node

        words = readwords("Words.txt")
        bintree = createtree(words)

        item = tree_find("other", bintree, False)

        minnode = find_min_node(item)

        self.assertEqual('matching', minnode.value)

    def test_delete_node_no_children(self):
        # Removing "a"
        print("\n\n Removing 'a', has no children")
        from Question2 import delete_node, createtree, readwords, printinorder, tree_find, gendot

        expected = ['add', 'and', 'and', 'and', 'box', 'can', 'choose', 'click', 'complement', 'cover', 'cover',
                    'designs', 'different', 'document', 'each', 'elements', 'example', 'footer', 'for', 'from',
                    'galleries', 'header', 'header', 'insert', 'look', 'make', 'matching', 'other', 'page', 'page',
                    'produced', 'professionally', 'provides', 'sidebar', 'text', 'that', 'the', 'the', 'then', 'to',
                    'want', 'word', 'you', 'you', 'your']

        words = readwords("Words.txt")
        bintree = createtree(words)
        nodetodelete = tree_find("a", bintree, False)
        if nodetodelete is False:
            self.assertFalse(True)
        else:
            print("In order before deletion \n", printinorder(bintree))
            print("Original\n" + gendot(bintree))
            delete_node(nodetodelete)
            print("In order after deleting the word 'box' \n", printinorder(bintree))
            print("After deletion\n" + gendot(bintree))
            self.assertEqual(expected, printinorder(bintree))

    def test_delete_node_one_child_left(self):
        # Removing "your" only has a left child
        print("\n\n Removing 'your', has one child")
        from Question2 import delete_node, createtree, readwords, printinorder, tree_find, gendot

        expected = ['a', 'add', 'and', 'and', 'and', 'box', 'can', 'choose', 'click', 'complement', 'cover', 'cover',
                    'designs', 'different', 'document', 'each', 'elements', 'example', 'footer', 'for', 'from',
                    'galleries', 'header', 'header', 'insert', 'look', 'make', 'matching', 'other', 'page', 'page',
                    'produced', 'professionally', 'provides', 'sidebar', 'text', 'that', 'the', 'the', 'then', 'to',
                    'want', 'word', 'you', 'you']

        words = readwords("Words.txt")
        bintree = createtree(words)
        nodetodelete = tree_find("your", bintree, False)
        if nodetodelete is False:
            try:
                self.fail(None)
            except AssertionError:
                pass
        else:
            print("In order before deletion \n", printinorder(bintree))
            print("Original\n" + gendot(bintree))
            print()
            delete_node(nodetodelete)
            print("In order after deleting the word box \n", printinorder(bintree))
            print("After deletion\n" + gendot(bintree))
            self.assertEqual(expected, printinorder(bintree))

    def test_delete_node_one_child_right(self):
        # Removing "provides" only has a right child
        print("\n\n Removing 'provides', has one child")
        from Question2 import delete_node, createtree, readwords, printinorder, tree_find, gendot

        expected = ['a', 'add', 'and', 'and', 'and', 'box', 'can', 'choose', 'click', 'complement', 'cover', 'cover',
                    'designs', 'different', 'document', 'each', 'elements', 'example', 'footer', 'for', 'from',
                    'galleries', 'header', 'header', 'insert', 'look', 'make', 'matching', 'other', 'page', 'page',
                    'produced', 'professionally', 'sidebar', 'text', 'that', 'the', 'the', 'then', 'to',
                    'want', 'word', 'you', 'you', 'your']

        words = readwords("Words.txt")
        bintree = createtree(words)
        nodetodelete = tree_find("provides", bintree, False)
        if nodetodelete is False:
            try:
                self.fail(None)
            except AssertionError:
                pass
        else:
            print("In order before deletion \n", printinorder(bintree))
            print("Original\n" + gendot(bintree))
            delete_node(nodetodelete)
            print("In order after deleting the word box \n", printinorder(bintree))
            print("After deletion\n" + gendot(bintree))
            self.assertEqual(expected, printinorder(bintree))

    def test_delete_node_two_children(self):
        # Removing "document" has two children
        print("\n\n Removing 'document', has two child")
        from Question2 import delete_node, createtree, readwords, printinorder, tree_find, gendot

        expected = ['a', 'add', 'and', 'and', 'and', 'box', 'can', 'choose', 'click', 'complement', 'cover', 'cover',
                    'designs', 'different', 'each', 'elements', 'example', 'footer', 'for', 'from',
                    'galleries', 'header', 'header', 'insert', 'look', 'make', 'matching', 'other', 'page', 'page',
                    'produced', 'professionally', 'provides', 'sidebar', 'text', 'that', 'the', 'the', 'then', 'to',
                    'want', 'word', 'you', 'you', 'your']

        words = readwords("Words.txt")
        bintree = createtree(words)
        nodetodelete = tree_find("document", bintree, False)
        if nodetodelete is False:
            try:
                self.fail(None)
            except AssertionError:
                pass
        else:
            print("In order before deletion \n", printinorder(bintree))
            print("Original\n" + gendot(bintree))
            delete_node(nodetodelete)
            print("In order after deleting the word box \n", printinorder(bintree))
            print("After deletion\n" + gendot(bintree))
            self.assertEqual(expected, printinorder(bintree))
