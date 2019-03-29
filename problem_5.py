#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Problem definition:

Write a program that outputs all possibilities to put + or - or nothing
between the numbers 1, 2, ..., 9 (in this order) such that the result
is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

"""
import sys
from itertools import zip_longest, permutations

import re

SEQUENCE = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def solve():
    for sequence in create_operator_combinations():
        calculate(create_equation(sequence))


def create_operator_combinations():
    operator_sequences = set()
    for combination in permutations("".join(["+" * 8, "-" * 8, "#" * 8]), 8):
        if combination not in operator_sequences:
            yield combination
            operator_sequences.add(combination)


def calculate(equation):
    if eval(equation) == 100:
        print("SUCCESS: equation {} equals 100".format(equation))


def create_equation(operator_combination):
    equation = ""
    for number, operator in zip_longest(SEQUENCE, operator_combination):
        if operator:
            equation += number + operator
        else:
            equation += number

    return re.sub("#", "", equation)


def main():
    solve()


if __name__ == '__main__':
    sys.exit(main())
