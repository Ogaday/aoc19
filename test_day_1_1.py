from abc import ABC
from unittest import TestCase

from day_1_1 import aggregate_fuel, calculate_fuel


class BaseFuelTest(ABC):
    def test_fuel_calc(self):
        self.assertEqual(calculate_fuel(self.mass), self.expected)


class TestMass0(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 12, 2


class TestMass1(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 14, 2


class TestMass2(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 1969, 654


class TestMass3(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 100756, 33583


class TestAggregateFuel(TestCase):
    def test(self):
        masses = [12, 14, 1969, 100756]
        output = aggregate_fuel(masses)
        expected = 34241
        self.assertEqual(output, expected)
