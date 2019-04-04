#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/no-idea/problem

"""

from collections import Counter
from itertools import zip_longest
import sys


class ProblemAttributes(object):
    N = 0
    M = 0
    elements = list()
    A = set()
    B = set()
    happiness = 0


def command_line():
    parse_first_line()
    parse_second_line()
    parse_third_line()
    parse_fourth_line()


def parse_first_line():
    nm = input().strip().split()
    ProblemAttributes.N = int(nm[0])
    ProblemAttributes.M = int(nm[1])
    assert 1 <= ProblemAttributes.N <= 1e5, \
        "N must be within range 1 <= N <= 1e5"
    assert 1 <= ProblemAttributes.M <= 1e5, \
        "N must be within range 1 <= N <= 1e5"


def parse_second_line():
    nm = input().strip().split()
    ProblemAttributes.elements = Counter(map(int, nm))
    assert all([1 <= element <= 1e9 for element in ProblemAttributes.elements]), \
        "Integer must be within range 1 <= integer <= 1e9"


def parse_third_line():
    nm = input().strip().split()
    ProblemAttributes.A = set(map(int, nm))
    assert all([1 <= element <= 1e9 for element in ProblemAttributes.A]), \
        "Integer must be within range 1 <= integer <= 1e9"
    assert len(ProblemAttributes.A) == ProblemAttributes.M, \
        "The size of set A must be equal to M"


def parse_fourth_line():
    nm = input().strip().split()
    ProblemAttributes.B = set(map(int, nm))
    assert all([1 <= element <= 1e9 for element in ProblemAttributes.B]), \
        "Integer must be within range 1 <= integer <= 1e9"
    assert len(ProblemAttributes.B) == ProblemAttributes.M, \
        "The size of set A must be equal to M"


def solve():
    a_diff = ProblemAttributes.A.difference(ProblemAttributes.B)
    b_diff = ProblemAttributes.B.difference(ProblemAttributes.A)
    for element_in_a, element_in_b in zip_longest(a_diff, b_diff):
        if element_in_a:
            ProblemAttributes.happiness += ProblemAttributes.elements[element_in_a]
        if element_in_b:
            ProblemAttributes.happiness -= ProblemAttributes.elements[element_in_b]

    print(ProblemAttributes.happiness)


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
