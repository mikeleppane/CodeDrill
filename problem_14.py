#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/word-order/problem

"""

from collections import Counter, OrderedDict
import sys


class ProblemAttributes(object):
    number_of_words = 0
    word_count = Counter()
    word_order = OrderedDict()


def command_line():
    parse_first_line()
    for _ in range(ProblemAttributes.number_of_words):
        word = input().rstrip()
        ProblemAttributes.word_count.update({word})
        ProblemAttributes.word_order.update(
            {word: ProblemAttributes.word_count[word]})


def parse_first_line():
    nm = input()
    ProblemAttributes.number_of_words = int(nm)
    assert 1 <= ProblemAttributes.number_of_words <= 1e5, \
        "Number of words must be within range 1 <= words <= 1e5"


def solve():
    print(len(ProblemAttributes.word_count.keys()))
    for word, count in ProblemAttributes.word_order.items():
        print(str(count) + " ", end='')


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
