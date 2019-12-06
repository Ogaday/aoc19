from unittest import TestCase

from day_6_2 import build_path, build_tree


class TestFindNode(TestCase):
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
                'K)YOU',
                'I)SAN',
            ]
        self.tree = build_tree(orbits)

    def test_find_you(self):
        path = build_path('COM', 'YOU', self.tree)
        expected = ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'YOU']
        self.assertEqual(path, expected)

    def test_find_san(self):
        path = build_path('COM', 'SAN', self.tree)
        expected = ['COM', 'B', 'C', 'D', 'I', 'SAN']
        self.assertEqual(path, expected)
