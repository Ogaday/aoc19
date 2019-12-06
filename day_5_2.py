"""
Solution to Day 5 Part II of the Advent of Code

https://adventofcode.com/2019/day/5

To get the answer, run:

    python -m day_5_2
"""
from typing import List

from day_5_1 import Instruction99, get, get_opcode, get_param_modes


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
                5: 2,
                6: 2,
                7: 3,
                8: 3,
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
            ) -> int:
        addrs = self.get_addresses(pos)
        if self.opcode == 1:
            memory[memory[addrs[2]]] = (
                    get(addrs[0], memory, self.modes[0])
                    + get(addrs[1], memory, self.modes[1])
                )
            return pos + self.num_params + 1
        elif self.opcode == 2:
            memory[memory[addrs[2]]] = (
                    get(addrs[0], memory, self.modes[0])
                    * get(addrs[1], memory, self.modes[1])
                )
            return pos + self.num_params + 1
        elif self.opcode == 3:
            memory[memory[addrs[0]]] = inputs.pop(0)
            return pos + self.num_params + 1
        elif self.opcode == 4:
            outputs.append(get(addrs[0], memory, self.modes[0]))
            return pos + self.num_params + 1
        elif self.opcode == 5:
            if get(addrs[0], memory, self.modes[0]):
                return get(addrs[1], memory, self.modes[1])
            else:
                return pos + self.num_params + 1
        elif self.opcode == 6:
            if get(addrs[0], memory, self.modes[0]) == 0:
                return get(addrs[1], memory, self.modes[1])
            else:
                return pos + self.num_params + 1
        elif self.opcode == 7:
            memory[memory[addrs[2]]] = int(
                    get(addrs[0], memory, self.modes[0])
                    < get(addrs[1], memory, self.modes[1])
                )
            return pos + self.num_params + 1
        elif self.opcode == 8:
            memory[memory[addrs[2]]] = int(
                    get(addrs[0], memory, self.modes[0])
                    == get(addrs[1], memory, self.modes[1])
                )
            return pos + self.num_params + 1
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
                pos = instruction(pos, self.memory, inputs, self.outputs)
            except Instruction99:
                break


if __name__ == "__main__":
    with open('input/day_5.txt') as f:
        program = [int(n) for n in f.read().strip().split(',')]
    c = Computer(program=program)
    c.run([5])
    print(c.outputs)
