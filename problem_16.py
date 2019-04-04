#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/iterables-and-iterators/problem

"""

from itertools import combinations
import sys


class ProblemAttributes(object):
    number_of_letters = 0
    letters = list()
    indices = 0


def command_line():
    parse_first_line()
    parse_second_line()
    parse_third_line()


def parse_first_line():
    nm = input()
    ProblemAttributes.number_of_letters = int(nm)
    assert 1 <= ProblemAttributes.number_of_letters <= 10, \
        "Number of letters must be within range 1 <= N <= 10"


def parse_second_line():
    ProblemAttributes.letters = input().rstrip().split()
    assert len(ProblemAttributes.letters) == ProblemAttributes.number_of_letters, \
        "Integer must be within range 1 <= integer <= 1e9"


def parse_third_line():
    nm = input()
    ProblemAttributes.indices = int(nm)
    assert 1 <= ProblemAttributes.indices <= ProblemAttributes.number_of_letters, \
        "indices must be within range 1 <= N <= {}".format(ProblemAttributes.number_of_letters)


def solve():
    indices = find_letter_a_indices()
    number_of_combinations = 0
    match_indices = 0
    for combination in combinations(
            range(
                1,
                ProblemAttributes.number_of_letters + 1),
            ProblemAttributes.indices):
        if any((number in indices for number in combination)):
            match_indices += 1
        number_of_combinations += 1

    print(match_indices / number_of_combinations)


def find_letter_a_indices():
    indices = set()
    for index, char in enumerate(ProblemAttributes.letters, start=1):
        if char == 'a':
            indices.add(index)
    return indices


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
