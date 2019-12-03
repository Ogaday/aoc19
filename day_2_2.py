"""
Solution to Day 2 Part II of the Advent of Code

https://adventofcode.com/2019/day/2

To get the answer, run:

    python -m day_2_2
"""
from itertools import product, zip_longest
from typing import List

from day_2_1 import OpCodeError


def computer(noun: int, verb: int, program: List[int]) -> int:
    memory = program.copy()
    memory[1], memory[2] = noun, verb
    for opcode, addr1, addr2, addr3 in zip_longest(*[iter(memory)] * 4):
        if opcode == 1:
            memory[addr3] = memory[addr1] + memory[addr2]
        elif opcode == 2:
            memory[addr3] = memory[addr1] * memory[addr2]
        elif opcode == 99:
            break
        else:
            raise OpCodeError(f'{opcode} is not a recognised opcode')

    return memory[0]


if __name__ == "__main__":
    with open('input/day_2.txt') as f:
        program = [int(n) for n in f.read().split(',')]

    desired = 19690720
    for (noun, verb) in product(range(100), repeat=2):
        if computer(noun, verb, program) == desired:
            break

    print(f'{noun=}, {verb=}, ans={100 * noun + verb}')
