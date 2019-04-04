#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/most-commons/problem

"""

from collections import Counter
from itertools import groupby
from operator import itemgetter
import sys


class ProblemAttributes(object):
    given_word = ""


def command_line():
    parse_first_line()


def parse_first_line():
    ProblemAttributes.given_word = input().rstrip()
    assert 3 < len(ProblemAttributes.given_word) <= 1e4, \
        "Given word size must be within range 3 < len(word) <= 1e4"


def solve():
    char_counter = Counter(ProblemAttributes.given_word)
    count = 1
    for key, group in groupby(sorted(char_counter.most_common(), key=itemgetter(1), reverse=True), itemgetter(1)):
        for pair in sorted(list(group), key=itemgetter(0)):
            if count > 3:
                break
            print("{} {}".format(*pair))
            count += 1


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
