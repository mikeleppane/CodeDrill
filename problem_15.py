#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/py-collections-deque/problem

"""

from collections import deque
import sys


class ProblemAttributes(object):
    number_of_operations = 0
    operations = list()
    operator_deque = deque()


def command_line():
    parse_first_line()
    for _ in range(ProblemAttributes.number_of_operations):
        action = input().rstrip().split()
        if len(action) == 2:
            ProblemAttributes.operations.append((action[0], action[1]))
        else:
            ProblemAttributes.operations.append((action[0], None))


def parse_first_line():
    nm = input()
    ProblemAttributes.number_of_operations = int(nm)
    assert 1 <= ProblemAttributes.number_of_operations <= 100, \
        "Number of operations must be within range 1 <= words <= 100"


def solve():
    print(ProblemAttributes.operations)
    for operation in ProblemAttributes.operations:
        if operation[0]:
            if operation[1]:
                getattr(ProblemAttributes.operator_deque, operation[0])(operation[1])
            else:
                getattr(ProblemAttributes.operator_deque, operation[0])()


def print_results():
    for _ in range(ProblemAttributes.number_of_operations):
        if ProblemAttributes.operator_deque:
            print(str(ProblemAttributes.operator_deque.popleft()) + " ", end='')


def main():
    command_line()
    solve()
    print_results()


if __name__ == '__main__':
    sys.exit(main())
