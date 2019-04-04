#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/collections-counter/problem

"""

from collections import Counter
import sys


class ProblemAttributes(object):
    number_of_shoes = 0
    shoes_sizes = list()
    number_of_customers = 0
    attribute_index = 0
    total = 0


def command_line():
    parse_first_line()
    parse_second_line()
    parse_third_line()
    for _ in range(ProblemAttributes.number_of_customers):
        size, price = tuple(map(int, input().rstrip().split()))
        if not 20 <= price <= 100:
            raise ValueError(
                "The value of a shoe must be within range 20 < price < 100")
        calculate(size, price)


def parse_first_line():
    nm = input()
    ProblemAttributes.number_of_shoes = int(nm)
    assert 0 < ProblemAttributes.number_of_shoes < 1000, \
        "Number of shoes must be within range 0 < number of shoes < 1000"


def parse_second_line():
    nm = input().strip().split()
    ProblemAttributes.shoes_sizes = Counter(map(int, nm))
    assert all([2 <= size <= 20 for size in ProblemAttributes.shoes_sizes.keys()]), \
        "All shoe sizes must be within range 2 < size < 20"


def parse_third_line():
    nm = input()
    ProblemAttributes.number_of_customers = int(nm)
    assert 0 < ProblemAttributes.number_of_customers <= 1000, \
        "Number of customers must be within range 0 < number of customers <= 1000"


def calculate(size, price):
    if size in ProblemAttributes.shoes_sizes:
        if ProblemAttributes.shoes_sizes[size] < 1:
            ProblemAttributes.shoes_sizes.pop(size)
            return
        ProblemAttributes.total += price
        ProblemAttributes.shoes_sizes[size] -= 1


def main():
    command_line()
    print(ProblemAttributes.total)


if __name__ == '__main__':
    sys.exit(main())
