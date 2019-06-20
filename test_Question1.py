from unittest import TestCase


class TestTree_Question1(TestCase):

    def test_readwords(self):
        from Question1 import readwords
        expected = ['to', 'make', 'your', 'document', 'look', 'professionally', 'produced', 'word', 'provides',
                    'header', 'footer', 'cover', 'page', 'and', 'text', 'box', 'designs', 'that', 'complement',
                    'each', 'other', 'for', 'example', 'you', 'can', 'add', 'a', 'matching', 'cover', 'page', 'header',
                    'and', 'sidebar', 'click', 'insert', 'and', 'then', 'choose', 'the', 'elements', 'you', 'want',
                    'from', 'the', 'different', 'galleries']
        self.assertEqual(readwords("Words.txt"), expected)

    def test_tree_create(self):
        from Question1 import createtree, readwords, printpreorder
        words = readwords("Words.txt")
        bintree = createtree(words)
        expected = ['to', 'make', 'document', 'cover', 'and', 'add', 'a', 'box', 'and', 'and', 'complement', 'can',
                    'click', 'choose', 'designs', 'cover', 'different', 'look', 'header', 'footer', 'each', 'example',
                    'elements', 'for', 'from', 'galleries', 'header', 'insert', 'professionally', 'produced', 'page',
                    'other', 'matching', 'page', 'provides', 'text', 'sidebar', 'that', 'then', 'the', 'the', 'your',
                    'word', 'want', 'you', 'you']
        self.assertEqual(printpreorder(bintree), expected)

    def test_tree_print_post_order(self):
        from Question1 import createtree, readwords, printpostorder
        words = readwords("Words.txt")
        bintree = createtree(words)
        expected = ['a', 'add', 'and', 'and', 'choose', 'click', 'can', 'complement', 'box', 'and', 'cover',
                    'different', 'designs', 'cover', 'elements', 'example', 'each', 'galleries', 'from', 'for',
                    'footer', 'insert', 'header', 'header', 'look', 'document', 'matching', 'other', 'page', 'page',
                    'produced', 'sidebar', 'the', 'the', 'then', 'that', 'text', 'provides', 'professionally', 'make',
                    'want', 'you', 'you', 'word', 'your', 'to']
        self.assertEqual(printpostorder(bintree), expected)

    def test_tree_print_in_order(self):
        from Question1 import createtree, readwords, printinorder
        words = readwords("Words.txt")
        bintree = createtree(words)
        expected = ['a', 'add', 'and', 'and', 'and', 'box', 'can', 'choose', 'click', 'complement', 'cover', 'cover',
                    'designs', 'different', 'document', 'each', 'elements', 'example', 'footer', 'for', 'from',
                    'galleries', 'header', 'header', 'insert', 'look', 'make', 'matching', 'other', 'page', 'page',
                    'produced', 'professionally', 'provides', 'sidebar', 'text', 'that', 'the', 'the', 'then', 'to',
                    'want', 'word', 'you', 'you', 'your']
        self.assertEqual(printinorder(bintree), expected)

    def test_find_in(self):
        from Question1 import createtree, readwords, tree_find
        words = readwords("Words.txt")
        bintree = createtree(words)
        expected = "look"
        self.assertEqual(tree_find("look", bintree, True).value, expected)

    def test_find_missing(self):
        from Question1 import createtree, readwords, tree_find
        words = readwords("Words.txt")
        bintree = createtree(words)
        expected = False
        try:
            actual = tree_find("missing", bintree, True).value
        except AttributeError:
            actual = False
        self.assertEqual(actual, expected)

    def test_tree_count(self):
        from Question1 import createtree, readwords, tree_count
        words = readwords("Words.txt")
        bintree = createtree(words)
        expected = {'a': 1, 'add': 1, 'and': 3, 'box': 1, 'can': 1, 'choose': 1, 'click': 1, 'complement': 1, 'cover': 2, 'designs': 1, 'different': 1, 'document': 1, 'each': 1, 'elements': 1, 'example': 1, 'footer': 1, 'for': 1, 'from': 1, 'galleries': 1, 'header': 2, 'insert': 1, 'look': 1, 'make': 1, 'matching': 1, 'other': 1, 'page': 2, 'produced': 1, 'professionally': 1, 'provides': 1, 'sidebar': 1, 'text': 1, 'that': 1, 'the': 2, 'then': 1, 'to': 1, 'want': 1, 'word': 1, 'you': 2, 'your': 1}

        self.assertEqual(tree_count(bintree), expected)
