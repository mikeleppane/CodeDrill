#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/matrix-script/problem

"""

import re
import sys


class Attributes(object):
    rows = 0
    columns = 0
    characters = list()
    raw_message = ""
    decoded_message = ""
    first_real_char = 0
    last_real_char = 0


attributes = Attributes()


def command_line():
    parse_first_line()
    for _ in range(attributes.rows):
        line = input()
        attributes.characters.append([line[index]
                                      for index in range(len(line))])


def solve():
    decode_script()


def parse_first_line():
    nm = input().split()
    attributes.rows = int(nm[0])
    attributes.columns = int(nm[1])
    assert 0 < attributes.rows, "Number of rows must be greater than 0"
    assert 1 <= attributes.columns < 100, "Number of rows must be less than 100"


def decode_script():
    flatten_character_array()
    compose_message()


def compose_message():
    sub_string = extract_sub_string()
    start = attributes.raw_message[0:attributes.first_real_char]
    middle = re.sub(r"\s\s+", " ", re.sub(r"\W", " ", sub_string))
    end = attributes.raw_message[attributes.last_real_char:]
    decoded_message = start + middle + end

    print(decoded_message)


def flatten_character_array():
    for j in range(attributes.columns):
        for i in range(attributes.rows):
            attributes.raw_message += attributes.characters[i][j]


def extract_sub_string():
    try:
        attributes.first_real_char = int(re.search(
            r"^\W*[A-Za-z0-9]",
            attributes.raw_message).end() - 1)
        attributes.last_real_char = int(re.search(
            r"[A-Za-z0-9]\W*$",
            attributes.raw_message).start())
    except AttributeError:
        attributes.first_real_char = 0
        attributes.last_real_char = 0
    return attributes.raw_message[attributes.first_real_char:attributes.last_real_char]


def main():
    command_line()
    solve()


if __name__ == '__main__':
    sys.exit(main())
