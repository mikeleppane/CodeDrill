#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Problem definition:

https://www.hackerrank.com/challenges/the-minion-game/problem

"""

import sys


class ProblemAttributes(object):
    game_word = ""
    vowels = ("A", "E", "I", "O", "U")
    stuart_strings = list()
    stuart_points = 0
    kevin_strings = list()
    kevin_points = 0


def command_line(s):
    ProblemAttributes.game_word = s
    assert 0 < len(
        ProblemAttributes.game_word
    ) <= 1e6, "Number of rows must be within range 1 <= rows <= 1000"


def solve():
    calculate_points(ProblemAttributes.game_word)
    define_winner()


def calculate_points(word):
    if not word:
        return
    for index in range(len(word)):
        starts_with_consonant = word[index].startswith(ProblemAttributes.vowels)
        if starts_with_consonant:
            ProblemAttributes.stuart_points += len(word[index:])
        else:
            ProblemAttributes.kevin_points += len(word[index:])


def define_winner():
    if ProblemAttributes.stuart_points > ProblemAttributes.kevin_points:
        print("Stuart {}".format(ProblemAttributes.stuart_points))
    elif ProblemAttributes.stuart_points < ProblemAttributes.kevin_points:
        print("Kevin {}".format(ProblemAttributes.kevin_points))
    else:
        print("Draw")


def minion_game(s):
    command_line(s)
    solve()


def main():
    command_line(input())
    solve()


if __name__ == '__main__':
    sys.exit(main())
