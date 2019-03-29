#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

Write a function that combines two lists by alternatingly taking elements.
For example: given the two lists [a, b, c] and [1, 2, 3], the function
should return [a, 1, b, 2, c, 3].

"""

import sys


def combine_lists_with_interleave(first, second):
    interleaved_sequence = list()
    for item_1, item_2 in zip(first, second):
        interleaved_sequence.extend((item_1, item_2))
    print("Interleaved sequence: {}".format(interleaved_sequence))


def main():
    first = ["a", "b", "c"]
    second = [1, 2, 3]
    combine_lists_with_interleave(first, second)


if __name__ == '__main__':
    sys.exit(main())
