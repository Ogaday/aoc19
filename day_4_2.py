"""
Solution to Day 4 Part II of the Advent of Code

https://adventofcode.com/2019/day/4

To get the answer, run:

    python -m day_4_2
"""
from typing import List

from day_4_1 import to_password


def has_double(password: List[int]) -> bool:
    """
    >>> has_double([1, 1, 2, 2, 3, 3])
    True
    >>> has_double([1, 2, 3, 4, 4, 4])
    False
    >>> has_double([1, 1, 1, 1, 2, 2])
    True
    """
    counts: List[int] = []
    last = None
    for p in password:
        if p == last:
            counts[-1] += 1
        else:
            counts.append(1)
        last = p
    return 2 in counts


def is_valid(password: List[int]) -> bool:
    """
    >>> is_valid([1, 1, 1, 1, 1, 1])
    False
    >>> is_valid([2, 2, 3, 4, 5, 0])
    False
    >>> is_valid([1, 2, 3, 7, 8, 9])
    False
    >>> is_valid([6, 6, 6, 5, 4, 0])
    False
    """
    is_monotonic = all(a <= b for a, b in zip(password[:-1], password[1:]))
    return has_double(password)and is_monotonic


def filter(passwords: List[List[int]]) -> List[List[int]]:
    return [password for password in passwords if is_valid(password)]


if __name__ == "__main__":
    with open('input/day_4.txt') as f:
        start, stop = [int(part) for part in f.read().strip().split('-')]

    passwords = [to_password(p) for p in range(start, stop + 1)]
    valid = filter(passwords)
    print(len(valid))
