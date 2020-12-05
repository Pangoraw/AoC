"""
Solution for day 05/12/2020
Created at 09:18:19 - 05/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines, map_input


def get_seat_id(seat):
    front = seat[:-3]
    back = seat[-3:]

    y = 0
    for i, c in enumerate(front):
        if c == "B":
            y += 2 ** (6 - i)

    x = 0
    for i, c in enumerate(back):
        if c == "R":
            x += 2**(2 - i)
    return x, y

def seat_id(S):
    x, y = S
    return y * 8 + x


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)

    return max([seat_id(get_seat_id(p)) for p in inp])


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    mat = [get_seat_id(p) for p in inp]
    X = [s[0] for s in mat]
    Y = [s[1] for s in mat]
    xmin, xmax = min(X), max(X)
    ymin, ymax = min(Y), max(Y)

    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            if (x, y) not in mat:
                return seat_id((x, y))

if __name__ == "__main__":
    CURRENT_DAY = 5
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
