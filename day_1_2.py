"""
Solution to Day 1 Part II of the Advent of Code

https://adventofcode.com/2019/day/1

To get the answer, run:

    python -m day_1_2
"""
from typing import List, TextIO

from day_1_1 import calculate_fuel


def compound_fuel(mass: int) -> int:
    """
    Given the mass of a module, calculate how much fuel it requires.

    This function accounts for the weight of the required fuel in addition to
    the weight of the module.
    """
    current_value = mass
    running_sum = 0
    while (current_value := calculate_fuel(current_value)) > 0:    # noqa
        running_sum += current_value

    return running_sum


def aggregate_fuel(masses: List[int]) -> int:
    """
    Given a list of module weights, find the total fuel required.

    This function accounts for the weight of the required fuel in addition to
    the weight of the module.
    """
    return sum(compound_fuel(mass) for mass in masses)


if __name__ == "__main__":
    filepath = 'input/day_1.txt'
    with open(filepath) as f:
        masses = [int(m) for m in f.read().split()]
    print(aggregate_fuel(masses))
