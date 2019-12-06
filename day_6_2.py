"""
Solution to Day 6 Part II of the Advent of Code

https://adventofcode.com/2019/day/6

To get the answer, run:

    python -m day_6_2
"""
from typing import Dict, List

from day_6_1 import Tree, build_tree


def build_path(current: str, saught: str, tree: Tree) -> List[str]:
    """
    Recursively find the path between current and saught.

    Uses depth first search to enumerate the tree until the saught after node
    is found. Returns the full path between current and saught.
    """
    if current == saught:
        return [current]
    for child in tree.get(current, []):
        if path := build_path(child, saught, tree):
            return [current] + path
    else:
        return []


if __name__ == "__main__":
    with open('input/day_6.txt') as f:
        orbits = f.read().split()
    tree = build_tree(orbits)
    path1 = build_path('COM', 'YOU', tree,)
    path2 = build_path('COM', 'SAN', tree,)
    disjoint = set(path1) ^ set(path2)
    print(len(disjoint) - 2)
