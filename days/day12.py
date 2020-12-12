"""
Solution for day 12/12/2020
Created at 10:48:35 - 12/12/20
"""

import sys
sys.path.append("../aoc")
from math import *

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    x, y, a = 0, 0, 0
    for inst in inp:
        d, v = inst[0], int(inst[1:])
        if d == "N":
            y += v
        if d == "S":
            y -= v
        if d == "E":
            x += v
        if d == "W":
            x -= v
        if d == "R":
            a -= v
        if d == "L":
            a += v
        if d == "F":
            x += int(v * cos(a * 2 * pi / 360))
            y += int(v * sin(a * 2 * pi / 360))

    return abs(x) + abs(y)

def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)

    wx, wy = 10, 1
    x, y, a = 0, 0, 0
    for inst in inp:
        d, v = inst[0], int(inst[1:])
        if d == "N":
            wy += v
        if d == "S":
            wy -= v
        if d == "E":
            wx += v
        if d == "W":
            wx -= v
        if d == "R":
            for i in range(v // 90):
                owx = wx
                wx = +wy
                wy = -owx
        if d == "L":
            for i in range(v // 90):
                owx = wx
                wx = -wy
                wy = +owx
        if d == "F":
            x += v * wx
            y += v * wy

    return abs(x) + abs(y)


if __name__ == "__main__":
    CURRENT_DAY = 12
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
