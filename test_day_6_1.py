from unittest import TestCase

from day_6_1 import build_tree, count_indirect


class TestBuildTree(TestCase):
    def setUp(self):
        orbits = [
                'COM)B',
                'B)C',
                'C)D',
                'D)E',
                'E)F',
                'B)G',
                'G)H',
                'D)I',
                'E)J',
                'J)K',
                'K)L',
            ]
        self.tree = build_tree(orbits)

    def test_num_noes(self):
        expected = 8
        self.assertEqual(len(self.tree), expected)

    def test_com_child(self):
        children = self.tree['COM']
        expected = ['B']
        self.assertEqual(children, expected)

    def test_no_children(self):
        with self.assertRaises(KeyError):
            self.tree['L']


class TestCountNodes(TestCase):
    def setUp(self):
        orbits = [
                'COM)B',
                'B)C',
                'C)D',
                'D)E',
                'E)F',
                'B)G',
                'G)H',
                'D)I',
                'E)J',
                'J)K',
                'K)L',
            ]
        self.tree = build_tree(orbits)

    def test_count_nodes(self):
        num_transitive_links = count_indirect('COM', self.tree)
        expected = 42
        self.assertEqual(num_transitive_links, expected)
