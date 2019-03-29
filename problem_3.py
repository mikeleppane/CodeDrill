#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Problem definition:

Write a function that computes the list of the first 100 Fibonacci numbers.
By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
and each subsequent number is the sum of the previous two. As an example,
here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

"""
import sys

COUNT_OF_FIBONACCI_NUMBERS = 100


def solve():
    print("The first {} Fibonacci numbers are: {}".format(
        COUNT_OF_FIBONACCI_NUMBERS, create_fibonacci_sequence()))


def create_fibonacci_sequence():
    ficonacci_numbers = [0, 1]
    for index in range(COUNT_OF_FIBONACCI_NUMBERS - 2):
        try:
            next_number = sum((
                ficonacci_numbers[index], ficonacci_numbers[index + 1]))
        except IndexError:
            break
        ficonacci_numbers.append(next_number)
    return ficonacci_numbers


def main():
    solve()


if __name__ == '__main__':
    sys.exit(main())
