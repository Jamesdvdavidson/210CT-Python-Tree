from unittest import TestCase


class Test_is_Path(TestCase):
    def test_add_node(self):
        from Question3 import addnode
        g = {}

        addnode(g, 2)
        self.assertEqual(g, {2: []})

        addnode(g, 3, [2])
        self.assertEqual(g, {2: [], 3: [2]})

        addnode(g, 1, [2, 3])
        self.assertEqual(g, {2: [], 3: [2], 1: [2, 3]})

    def test_is_path(self):
        from Question3 import addnode, ispath

        g = {}

        g = addnode(g, 0, [1])
        g = addnode(g, 1, [2, 6])
        g = addnode(g, 2, [1, 3, 4, 9])
        g = addnode(g, 3, [2])
        g = addnode(g, 4, [2, 5])
        g = addnode(g, 5, [4])
        g = addnode(g, 6, [1, 8])
        g = addnode(g, 7, [6])
        g = addnode(g, 8, [6])
        g = addnode(g, 9, [2])

        self.assertEqual([3, 2, 1, 6, 8], ispath(g, 3, 8))

    def test_is_path_none(self):
        from Question3 import addnode, ispath

        g = {}

        g = addnode(g, 0, [])
        g = addnode(g, 1, [2, 6])
        g = addnode(g, 2, [1, 3, 4, 9])
        g = addnode(g, 3, [2])
        g = addnode(g, 4, [2, 5])
        g = addnode(g, 5, [4])
        g = addnode(g, 6, [1, 8])
        g = addnode(g, 7, [6])
        g = addnode(g, 8, [6])
        g = addnode(g, 9, [2])

        self.assertEqual(None, ispath(g, 4, 0))
