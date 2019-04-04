#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/ginorts/problem

"""

import re
import sys


class ProblemAttributes(object):
    given_word = ""


def command_line():
    parse_first_line()


def parse_first_line():
    ProblemAttributes.given_word = input().rstrip()
    assert 1 <= len(ProblemAttributes.given_word) < 1000, \
        "Given word size  must be within range 0 < words < 1000"


def solve():
    upper_cases = "".join(sorted(re.findall(r"[A-Z]", ProblemAttributes.given_word)))
    lower_cases = "".join(sorted(re.findall(r"[a-z]", ProblemAttributes.given_word)))
    uneven_digits = "".join(sorted(re.findall(r"[13579]", ProblemAttributes.given_word)))
    even_digits = "".join(sorted(re.findall(r"[02468]", ProblemAttributes.given_word)))
    print("".join([lower_cases, upper_cases, uneven_digits, even_digits]))


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
