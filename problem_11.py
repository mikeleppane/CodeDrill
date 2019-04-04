#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/any-or-all/problem

"""

import sys


class ProblemAttributes(object):
    number_of_ints = 0
    numbers = list()


def command_line():
    parse_first_line()
    parse_second_line()


def parse_first_line():
    nm = input()
    ProblemAttributes.number_of_ints = int(nm)
    assert 0 < ProblemAttributes.number_of_ints < 100, \
        "Number of ints must be within range 0 < number of ints < 100"


def parse_second_line():
    nm = input().strip().split()
    ProblemAttributes.numbers = list(map(int, nm))
    assert len(ProblemAttributes.numbers) == ProblemAttributes.number_of_ints, \
        "Given number of integers does not match expected number of ints"


def calculate():
    return is_all_integer_positive() and is_palindromic_number()


def is_all_integer_positive():
    if all((number >= 0 for number in ProblemAttributes.numbers)):
        return True
    return False


def is_palindromic_number():
    return any((number == reverse_number(number) for number in ProblemAttributes.numbers))


def reverse_number(number):
    return int(str(number)[len(str(number)):None:-1])


def main():
    command_line()
    print(calculate())


if __name__ == '__main__':
    sys.exit(main())
