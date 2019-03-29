#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Problem definition:

Write a function that given a list of non negative integers,
arranges them such that they form the largest possible number.
For example, given [50, 2, 1, 9], the largest formed number is 95021.

"""
import sys


def solve(numbers):
    largest_number = sorted(numbers, key=lambda value: str(value), reverse=True)
    print("The largest number in sequence {} is {}".format(numbers, form_number(largest_number)))


def form_number(combination_sequence):
    return int("".join(map(str, combination_sequence)))


def validate_numbers_are_nonnegative(numbers):
    for number in numbers:
        assert int(number) >= 0, "given number {} must non negative".format(number)


def map_numbers_to_int(values):
    return [int(value) for value in values.split(",")]


def main(numbers):
    numbers = map_numbers_to_int(numbers)
    validate_numbers_are_nonnegative(numbers)
    solve(numbers)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
