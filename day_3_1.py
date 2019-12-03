"""
Solution to Day 3 Part I of the Advent of Code

https://adventofcode.com/2019/day/3

To get the answer, run:

    python -m day_3_1
"""
from typing import List


class Coord:
    """
    Coordinate object

    >>> p = Coord(1, 2)
    >>> q = Coord(1, -1)
    >>> p + q
    Coord(x=2, y=1)
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object):
        if not isinstance(other, Coord):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return f'Coord(x={self.x}, y={self.y})'

    def __hash__(self):
        return hash((self.x, self.y))


# Fundamental units:
BASIS = {
        'R': Coord(1, 0),
        'U': Coord(0, 1),
        'L': Coord(-1, 0),
        'D': Coord(0, -1),
    }

ORIGIN = Coord(0, 0)


def get_coordinates(instructions):
    """
    >>> instructions = ['R1', 'U2', 'L1', 'D2']
    >>> list(get_coordinates(instructions))
    [Coord(x=0, y=0), Coord(x=1, y=0), Coord(x=1, y=1), Coord(x=1, y=2),
     Coord(x=0, y=2), Coord(x=0, y=1), Coord(x=0, y=0)]
    """
    current = Coord(0, 0)
    yield current
    for inst in instructions:
        direction = BASIS[inst[0]]
        magnitude = int(inst[1:])
        for i in range(1, magnitude + 1):
            current += direction
            yield current


def get_intersects(inst1: List[str], inst2: List[str]) -> set:
    """
    Given two instruction sets, find all points of intersection.

    >>> inst1 = ['R1', 'U2']
    >>> inst2 = ['U1', 'R2']
    >>> get_intersects(inst1, inst2)
    {Coord(x=1, y=1)}
    """
    intersects = set(get_coordinates(inst1)) & set(get_coordinates(inst2))
    intersects -= {ORIGIN}
    return intersects


def manhattan(start: Coord, stop: Coord) -> int:
    """
    Calculate the manhattan distance between two coordinates.

    >>> p = Coord(13, 2)
    >>> q = Coord(25, 40)
    >>> manhattan(p, q)
    50
    """
    return abs(start.x - stop.x) + abs(start.y - stop.y)


def main(inst1: List[str], inst2: List[str]) -> int:
    """
    Find the intersection closest to the origina by Manhattan distance.
    """
    intersects = get_intersects(inst1, inst2)
    distances = [manhattan(ORIGIN, coord) for coord in intersects]
    return min(distances)


if __name__ == "__main__":
    with open('input/day_3.txt') as f:
        inst1, inst2 = [row.split(',') for row in f.read().split()]
    print(main(inst1, inst2))
