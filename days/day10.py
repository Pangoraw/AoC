"""
Solution for day 10/12/2020
Created at 08:54:45 - 10/12/20
"""

import sys
sys.path.append("../aoc")
from functools import lru_cache

from aoc import challenge_runner
from aoc.parser import get_lines, map_input


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = sorted(map_input(inp, int))
    diff = [a - b for a, b in zip(inp, [0] + inp[:-1])]
    return sum(a == 1 for a in diff) * (sum(a == 3 for a in diff) + 1)


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = sorted(map_input(inp, int))
    inp = [0] + inp + [max(inp) + 3]

    @lru_cache(maxsize=32)
    def arr(idx):
        if idx == len(inp) - 1:
            return 1
        k = 1
        s = 0
        while idx + k < len(inp) and inp[idx + k] - inp[idx] <= 3:
            s += arr(idx + k)
            k += 1

        return s

    return arr(0)

if __name__ == "__main__":
    CURRENT_DAY = 10
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
