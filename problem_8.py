#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/python-sort-sort/problem

"""

from operator import itemgetter
import sys


class ProblemAttributes(object):
    rows = 0
    columns = 0
    data_matrix = list()
    attribute_index = 0


def command_line():
    parse_first_line()
    for _ in range(ProblemAttributes.rows):
        values = list(map(int, input().rstrip().split()))
        if not all((value <= 1000 for value in values)):
            raise ValueError(
                "Each value in row must less than or equal to 1000")
        ProblemAttributes.data_matrix.append(values)
    parse_last_line()


def parse_first_line():
    nm = input().split()
    ProblemAttributes.rows = int(nm[0])
    ProblemAttributes.columns = int(nm[1])
    assert 1 <= ProblemAttributes.rows <= 1000, "Number of rows must be within range 1 <= rows <= 1000"
    assert 1 <= ProblemAttributes.columns < 1000, "Number of rows must be within range 1 <= columns <= 1000"


def parse_last_line():
    ProblemAttributes.attribute_index = int(input())
    assert 0 <= ProblemAttributes.attribute_index < ProblemAttributes.columns, \
        "The attribute index must be within range 1 <= index < column"


def solve():
    print_result(sort_data_matrix())


def sort_data_matrix():
    return sorted(
        ProblemAttributes.data_matrix, key=itemgetter(
            ProblemAttributes.attribute_index))


def print_result(result_matrix):
    for row in result_matrix:
        print(*row)


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
