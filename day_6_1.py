"""
Solution to Day 6 Part I of the Advent of Code

https://adventofcode.com/2019/day/6

To get the answer, run:

    python -m day_6_1
"""
from typing import Dict, List


Tree = Dict[str, List[str]]


def build_tree(orbits: List[str]) -> Tree:
    """
    Parse a list of dependencies in an easily navigable tree structure.
    """
    tree: Tree = {}
    for orbit in orbits:
        centre, satellite = orbit.split(')')
        try:
            tree[centre].append(satellite)
        except KeyError:
            tree[centre] = [satellite]

    return tree


def count_indirect(current: str, tree: Tree, depth: int = 0) -> int:
    """
    Count all transitive dependencies on the current node in a tree.
    """
    if children := tree.get(current, []):
        return (
                sum(
                    count_indirect(child, tree, depth + 1)
                    for child in children
                )
                + depth
            )
    else:
        return depth


if __name__ == "__main__":
    with open('input/day_6.txt') as f:
        orbits = f.read().split()
    print(count_indirect('COM', build_tree(orbits)))
