from unittest import TestCase

from day_2_1 import run, OpCodeError


class TestRun(TestCase):
    def test_run_0(self):
        program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        run(program)
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertListEqual(program, expected)

    def test_run_1(self):
        program = [1, 0, 0, 0, 99]
        run(program)
        expected = [2, 0, 0, 0, 99]
        self.assertListEqual(program, expected)

    def test_run_2(self):
        program = [2, 3, 0, 3, 99]
        run(program)
        expected = [2, 3, 0, 6, 99]
        self.assertListEqual(program, expected)

    def test_run_3(self):
        program = [2, 4, 4, 5, 99, 0]
        run(program)
        expected = [2, 4, 4, 5, 99, 9801]
        self.assertListEqual(program, expected)

    def test_run_4(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        run(program)
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertListEqual(program, expected)

    def test_raises_opcode_error(self):
        program = [3, 0, 0, 0, 99]
        with self.assertRaises(OpCodeError):
            run(program)
