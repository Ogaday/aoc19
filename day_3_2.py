"""
Solution to Day 3 Part II of the Advent of Code

https://adventofcode.com/2019/day/3

To get the answer, run:

    python -m day_3_2
"""
from typing import Dict, List, Set

from day_3_1 import Coord, get_coordinates, get_intersects


def get_distances(instructions: List[str], intersections: set) -> dict:
    """
    Find all distances from the origin to the intersections between two paths.

    Distance is calculated as each step along both paths leading to the
    intersection.
    """
    distances: Dict[Coord, int] = dict()
    seen: Set[Coord] = set()
    running_distance = 0
    for coord in get_coordinates(instructions):
        if coord in intersections and coord not in seen:
            distances[coord] = running_distance
            seen.add(coord)
        running_distance += 1

    return distances


def main(inst1: List[str], inst2: List[str]) -> int:
    """
    Find the shortest total distance to any intersection from the origin.

    Distance is calculated as each step along both paths leading to the
    intersection.
    """
    intersections = get_intersects(inst1, inst2)

    dist1 = get_distances(inst1, intersections)
    dist2 = get_distances(inst2, intersections)

    distances = [dist1[coord] + dist2[coord] for coord in intersections]

    return min(distances)


if __name__ == "__main__":
    with open('input/day_3.txt') as f:
        inst1, inst2 = [row.split(',') for row in f.read().split()]
    print(main(inst1, inst2))
