"""
Solution for day 25/12/2020
Created at 13:05:22 - 25/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    pkc, pkd = map(int, inp)

    pk = pkc
    bwd = []
    ls = 0
    while pk != 1:
        ls += 1
        N = 0
        new_pk = (N * 20201227 + pk)
        while new_pk % 7 != 0:
            N += 1
            new_pk = (N * 20201227 + pk)
        pk = new_pk // 7
        bwd.append(pk)

    v = 1
    for _ in range(ls):
        v *= pkd
        v = v % 20201227
    return v


def solution2(inp):
    """Solves the second part of the challenge"""
    return "done"


if __name__ == "__main__":
    CURRENT_DAY = 25
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
