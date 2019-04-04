#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/compress-the-string/problem

"""

from itertools import groupby
import sys


class ProblemAttributes(object):
    input_string = ""
    results = list()


def command_line():
    parse_first_line()


def parse_first_line():
    nm = input()
    ProblemAttributes.input_string = nm
    assert 1 <= len(ProblemAttributes.input_string) <= 1e4, \
        "The size of the input string must be within range 1 <= size of string < 1e4"


def calculate():
    for key, group in groupby(ProblemAttributes.input_string):
        try:
            ProblemAttributes.results.append((len(list(group)), int(key)))
        except ValueError:
            ProblemAttributes.results.append((len(list(group)), key))

    print(*ProblemAttributes.results)


def main():
    command_line()


if __name__ == '__main__':
    sys.exit(main())
