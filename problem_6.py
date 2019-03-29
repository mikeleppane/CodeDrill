#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/maximize-it/problem

"""

from collections import deque
import sys


class Attributes(object):
    K = 0
    M = 0
    S_MAX = 0
    arrays = list()
    BUFFER = deque()


attributes = Attributes()


def command_line():
    line_number = 0
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        if line_number == 0:
            parse_first_line(line)
        else:
            parse_element_list(line)
        line_number += 1


def sort_array():
    attributes.arrays = sorted(
        attributes.arrays,
        key=lambda x: len(x),
        reverse=True)


def parse_first_line(line):
    attributes.K, attributes.M = map(int, line.split(" "))
    assert 1 <= attributes.K <= 7, "Number of lists must be within range 1 <= K <= 7"
    assert 1 <= attributes.M <= 1000, "Module must be within 1 <= M <= 1000"


def parse_element_list(line):
    elements = [int(element) for element in line.split(" ")]
    assert elements[0] == len(elements[1:]), "Mismatch: the first element in list {} " \
                                             "denotes number of remaining items {}.".\
        format(elements[0], len(elements[1:]))
    verify_values_within_range(elements[1:])
    attributes.arrays.append(elements[1:])


def verify_values_within_range(values):
    if not all([1 <= value <= 1e9 for value in values]):
        raise AssertionError(
            "Magnitude of value must be within 1 <= value <= 1e9")


def do_calculation():
    sort_array()
    for item in attributes.arrays[0]:
        attributes.BUFFER.clear()
        attributes.BUFFER.append(power_of_two_with_modulo(item))
        if attributes.arrays[1:]:
            walk(attributes.arrays[1:])
        else:
            calculate_max_module()

    print(attributes.S_MAX)


def walk(array):
    if len(array) == 1:
        for item in array[0]:
            attributes.BUFFER.append(power_of_two_with_modulo(item))
            calculate_max_module()
            attributes.BUFFER.pop()
        return
    else:
        for item in array[0]:
            attributes.BUFFER.append(power_of_two_with_modulo(item))
            walk(array[1:])
            attributes.BUFFER.pop()


def power_of_two_with_modulo(value):
    return value ** 2 % attributes.M


def calculate_max_module():
    attributes.S_MAX = max(
        attributes.S_MAX,
        sum(attributes.BUFFER) % attributes.M)


def main():
    command_line()
    do_calculation()


if __name__ == '__main__':
    sys.exit(main())
