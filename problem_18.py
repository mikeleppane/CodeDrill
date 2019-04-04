#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/piling-up/problem

"""

from collections import deque
import sys


class ProblemAttributes(object):
    number_of_test_cases = 0
    results = list()
    cube_size_first_on_stack = 0


def command_line():
    parse_first_line()
    for _ in range(ProblemAttributes.number_of_test_cases):
        number_of_cubes = int(input())
        assert 1 <= number_of_cubes <= 1e5, \
            "Number of cubes must be within range 1 <= N <= 1e5"
        cude_sides = deque(list(map(int, input().rstrip().split())))
        assert all((1 <= side <= 2**31 for side in cude_sides)), \
            "Cube side must be within range 1 <= N <= 2^31"
        assert number_of_cubes == len(cude_sides), \
            "Given number of cubes mismatch to expected cubes: {} != {}".format(number_of_cubes,
                                                                                len(cude_sides))
        solve_test_case(cude_sides)


def parse_first_line():
    nm = input()
    ProblemAttributes.number_of_test_cases = int(nm)
    assert 1 <= ProblemAttributes.number_of_test_cases <= 5, \
        "Number of test cases must be within range 1 <= N <= 5"


def solve_test_case(cubes):
    can_stack = "Yes"
    ProblemAttributes.cube_size_first_on_stack = 2 ** 31
    while len(cubes) > 0:
        if len(cubes) > 1:
            first = cubes[0]
            last = cubes[-1]
            is_ok_to_stop = ProblemAttributes.cube_size_first_on_stack < first and \
                ProblemAttributes.cube_size_first_on_stack < last
            if is_ok_to_stop:
                can_stack = "No"
                break
            if last <= first <= ProblemAttributes.cube_size_first_on_stack:
                ProblemAttributes.cube_size_first_on_stack = cubes.popleft()
            elif ProblemAttributes.cube_size_first_on_stack >= last:
                ProblemAttributes.cube_size_first_on_stack = cubes.pop()
            else:
                can_stack = "No"
                break
        else:
            last = cubes[0]
            if ProblemAttributes.cube_size_first_on_stack < last:
                can_stack = "No"
            break

    ProblemAttributes.results.append(can_stack)


def main():
    command_line()
    for result in ProblemAttributes.results:
        print(result)


if __name__ == '__main__':
    sys.exit(main())
