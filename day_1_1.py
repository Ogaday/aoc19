"""
Solution to Day 1 Part I of the Advent of Code

https://adventofcode.com/2019/day/1

To get the answer, run:

    python -m day_1_1
"""
from typing import List


def calculate_fuel(mass: int) -> int:
    """
    Given the mass of a module, calculate how much fuel it requires
    """
    return mass // 3 - 2


def aggregate_fuel(masses: List[int]) -> int:
    """
    Given a list of module weights, find the total fuel required.
    """
    return sum(calculate_fuel(mass) for mass in masses)


if __name__ == "__main__":
    filepath = 'input/day_1.txt'
    with open(filepath) as f:
        masses = [int(m) for m in f.read().split()]
    print(aggregate_fuel(masses))
