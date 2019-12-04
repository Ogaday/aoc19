"""
Solution to Day 4 Part I of the Advent of Code

https://adventofcode.com/2019/day/4

To get the answer, run:

    python -m day_4_1
"""
from typing import List


def is_valid(password: List[int]) -> bool:
    """
    >>> is_valid([1, 1, 1, 1, 1, 1])
    True
    >>> is_valid([2, 2, 3, 4, 5, 0])
    False
    >>> is_valid([1, 2, 3, 7, 8, 9])
    False
    >>> is_valid([6, 6, 6, 5, 4, 0])
    False
    """
    has_double = any(a == b for a, b in zip(password[:-1], password[1:]))
    is_monotonic = all(a <= b for a, b in zip(password[:-1], password[1:]))
    return has_double and is_monotonic


def filter(passwords: List[List[int]]) -> List[List[int]]:
    return [password for password in passwords if is_valid(password)]


def to_num(password: List[int]) -> int:
    """
    >>> to_num([1, 2, 3])
    123
    >>> to_num([3, 4, 1, 8, 6, 7])
    341867
    """
    return sum(
            [p * 10**(len(password) - 1 - i) for i, p in enumerate(password)]
        )


def to_password(num: int, places: int = 6) -> List[int]:
    """
    >>> to_password(123, places=3)
    [1, 2, 3]
    >>> to_password(123)
    [0, 0, 0, 1, 2, 3]
    """
    return [
            num % 10 ** (places - i) // 10 ** (places - 1 - i)
            for i in range(places)
        ]


if __name__ == "__main__":
    with open('input/day_4.txt') as f:
        start, stop = [int(part) for part in f.read().strip().split('-')]

    passwords = [to_password(p) for p in range(start, stop + 1)]
    valid = filter(passwords)
    print(len(valid))
