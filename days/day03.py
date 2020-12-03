"""
Solution for day 03/12/2020
Created at 08:29:01 - 03/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines, map_input


def count_trees(inp, sl):
    dx, dy = sl
    w = len(inp[0])
    h = len(inp)

    x = 0
    y = 0
    s = 0
    while y != h:
        if inp[y][x % w] == "#":
            s += 1
        x += dx
        y += dy
        y = min(h, y)
    return s


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)

    s = count_trees(inp, (3, 1))

    return s


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    s = 1
    for sl in slopes:
        n = count_trees(inp, sl)
        print(sl, n)
        s *= n
    return s


if __name__ == "__main__":
    CURRENT_DAY = 3
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
