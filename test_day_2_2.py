from unittest import TestCase

from day_2_2 import computer, OpCodeError


class TestComputer(TestCase):
    def test_case_1(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        output = computer(1, 1, program)
        expected = 30
        self.assertEqual(output, expected)

    def test_raises_opcode_error(self):
        program = [3, 0, 0, 0, 99]
        with self.assertRaises(OpCodeError):
            computer(1, 1, program)
