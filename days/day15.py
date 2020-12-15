"""
Solution for day 15/12/2020
Created at 09:05:11 - 15/12/20
"""

import sys
sys.path.append("../aoc")
from collections import defaultdict

from aoc import challenge_runner
from aoc.parser import get_lines


def solve(inp, N):
    num = inp.split(",")
    num = list(map(int, num))
    said = {n: [i] for i, n in enumerate(num)}

    last = num[-1]
    for i in range(len(num), N):
        if len(said[last]) == 1:
            said[0].append(i)
            last = 0
        else:
            b, c = said[last][-2:]
            n = c - b
            if n in said:
                said[n].append(i)
            else:
                said[n] = [i]
            last = n
    return n


def solution1(inp):
    """Solves the first part of the challenge"""
    return solve(inp, 2020)


def solution2(inp):
    """Solves the second part of the challenge"""
    return solve(inp, 30_000_000)


if __name__ == "__main__":
    CURRENT_DAY = 15
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
