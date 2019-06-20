from unittest import TestCase


class test_question5(TestCase):

    def test_dfs(self):
        from Question3 import addnode
        from Question5 import dfstofile

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

        self.assertEqual(dfstofile(g, 0), [0, 1, 2, 3, 4, 5, 9, 6, 7, 8])
        self.assertEqual(dfstofile(g, 4), [4, 2, 1, 0, 7, 6, 8, 3, 9, 5])

    def test_bfs(self):
        from Question3 import addnode
        from Question5 import bfs

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

        self.assertEqual(bfs(g, 0), [8, 6, 1, 7, 0, 2, 3, 4, 9, 5])
        self.assertEqual(bfs(g, 5), [5, 4, 2, 1, 3, 9, 0, 6, 7, 8])
