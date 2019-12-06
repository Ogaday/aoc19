"""
Solution to Day 5 Part I of the Advent of Code

https://adventofcode.com/2019/day/5

To get the answer, run:

    python -m day_5_1
"""
from enum import Enum
from typing import List


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Instruction99(Exception):
    """
    Raised to terminate a program
    """


def get_opcode(code: int) -> int:
    """
    >>> get_opcode(1002)
    2
    >>> get_opcode(1099)
    99
    """
    return code % 100


def get_param_modes(code: int, num_params: int) -> List[Mode]:
    """
    >>> get_param_modes(1002, 3)
    [<Mode.POSITION: 0>, <Mode.IMMEDIATE: 1>, <Mode.POSITION: 0>]
    >>> get_param_modes(1102, 3)
    [<Mode.IMMEDIATE: 1>, <Mode.IMMEDIATE: 1>, <Mode.POSITION: 0>]
    """
    code = code // 100
    return [Mode(code % 10 ** (i + 1) // 10 ** i) for i in range(num_params)]


def get(address: int, memory: List[int], mode: Mode) -> int:
    """
    >>> get(3, [1, 2, 3, 1, 5], mode=Mode.POSITION)
    2
    >>> get(3, [1, 2, 3, 1, 5], mode=Mode.IMMEDIATE)
    1
    """
    if mode == Mode.POSITION:
        return memory[memory[address]]
    elif mode == Mode.IMMEDIATE:
        return memory[address]
    else:
        raise ValueError(f"{mode}")


class Instruction:
    def __init__(self, code: int):
        """
        Initialise an instruction based upon a code
        """
        self.opcode = get_opcode(code)
        self.modes = get_param_modes(code, self.num_params)

    @property
    def num_params(self) -> int:
        num_params = {
                1: 3,
                2: 3,
                3: 1,
                4: 1,
                99: 0,
            }
        return num_params[self.opcode]

    def get_addresses(self, pos: int) -> List[int]:
        return [pos + i for i in range(1, self.num_params + 1)]

    def __call__(
            self,
            pos: int,
            memory: List[int],
            inputs: List[int],
            outputs:
            List[int]
            ):
        addrs = self.get_addresses(pos)
        if self.opcode == 1:
            memory[memory[addrs[2]]] = (
                    get(addrs[0], memory, self.modes[0])
                    + get(addrs[1], memory, self.modes[1])
                )
        elif self.opcode == 2:
            memory[memory[addrs[2]]] = (
                    get(addrs[0], memory, self.modes[0])
                    * get(addrs[1], memory, self.modes[1])
                )
        elif self.opcode == 3:
            memory[memory[addrs[0]]] = inputs.pop(0)
        elif self.opcode == 4:
            outputs.append(get(addrs[0], memory, self.modes[0]))
        elif self.opcode == 99:
            raise Instruction99
        else:
            raise Exception("Unrecognised opcode: {self.opcode}")


class Computer:
    def __init__(self, program: List[int]):
        self.program = program
        self.memory = program[:]
        self.outputs: List[int] = []

    def run(self, inputs: List[int]):
        """
        >>> c = Computer([3, 0, 4, 0, 99])
        >>> c.run([100])
        >>> c.memory
        [100, 0, 4, 0, 99]
        >>> c.outputs
        [100]
        """
        # set up:
        self.memory = self.program[:]
        inputs = inputs[:]
        pos = 0

        # run:
        while pos < len(self.memory):
            instruction = Instruction(self.memory[pos])
            try:
                instruction(pos, self.memory, inputs, self.outputs)
            except Instruction99:
                break
            pos += instruction.num_params + 1


if __name__ == "__main__":
    with open('input/day_5.txt') as f:
        program = [int(n) for n in f.read().strip().split(',')]
    c = Computer(program=program)
    c.run([1])
    print(c.outputs)
