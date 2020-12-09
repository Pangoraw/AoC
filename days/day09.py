"""
Solution for day 09/12/2020
Created at 08:00:05 - 09/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    inp = list(map(int, inp))

    for i, n in enumerate(inp[25:]):
        if not any(n - k in inp[i:i+25]
                   for k in inp[i:i+25]):
            return n
    return inp


def solution2(inp):
    """Solves the second part of the challenge"""
    s1 = solution1(inp)

    inp = get_lines(inp)
    inp = list(map(int, inp))

    for i, n in enumerate(inp):
        k = 2
        s = sum(inp[i:i+k])
        while s < s1:
            k += 1
            s = sum(inp[i:i+k])
        if s == s1:
            nmin, nmax = min(inp[i:i+k]), max(inp[i:i+k])
            return nmin + nmax


if __name__ == "__main__":
    CURRENT_DAY = 9
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
