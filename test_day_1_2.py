from abc import ABC
from unittest import TestCase

from day_1_2 import aggregate_fuel, compound_fuel


class BaseFuelTest(ABC):
    def test_fuel_calc(self):
        self.assertEqual(compound_fuel(self.mass), self.expected)


class TestMass0(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 14, 2


class TestMass1(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 1969, 966


class TestMass2(BaseFuelTest, TestCase):
    def setUp(self):
        self.mass, self.expected = 100756, 50346


class TestAggregateFuel(TestCase):
    def test(self):
        masses = [12, 14, 1969, 100756]
        output = aggregate_fuel(masses)
        expected = 51316
        self.assertEqual(output, expected)
