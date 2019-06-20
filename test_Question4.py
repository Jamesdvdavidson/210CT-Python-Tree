from unittest import TestCase


class test_is_question4(TestCase):
    def test_is_strongly_connected_true(self):
        from Question4 import isConnected, addnode

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

        self.assertEqual(isConnected(g, 0), "Yes")

    def test_is_strongly_connected_false(self):
        from Question4 import isConnected, addnode

        g = {}

        g = addnode(g, 0, [1, 2])
        g = addnode(g, 1, [0, 2])
        g = addnode(g, 2, [0, 1])

        g = addnode(g, 4, [5, 6])
        g = addnode(g, 5, [4, 6])
        g = addnode(g, 6, [4, 5, 6])

        self.assertEqual(isConnected(g, 0), "No")
        self.assertEqual(isConnected(g, 4), "No")
