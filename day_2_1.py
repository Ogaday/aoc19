"""
Solution to Day 2 Part I of the Advent of Code

https://adventofcode.com/2019/day/2

To get the answer, run:

    python -m day_2_1
"""
from itertools import zip_longest
from typing import List


class OpCodeError(Exception):
    """
    Raise when an invalid opcode is encountered.
    """


def run(intcode: List[int]) -> None:
    """
    Process an intcode program.

    Mutates the input in place - does not return the modified program.
    """
    for opcode, arg1, arg2, output in zip_longest(*[iter(intcode)] * 4):
        if opcode == 1:
            intcode[output] = intcode[arg1] + intcode[arg2]
        elif opcode == 2:
            intcode[output] = intcode[arg1] * intcode[arg2]
        elif opcode == 99:
            break
        else:
            raise OpCodeError(f'{opcode=} is not a recognised opcode')


if __name__ == "__main__":
    with open('input/day_2.txt') as f:
        program = [int(n) for n in f.read().split(',')]
    program[1] = 12
    program[2] = 2
    run(program)
    print(program[0])
