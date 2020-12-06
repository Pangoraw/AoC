"""
Solution for day 06/12/2020
Created at 10:42:53 - 06/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines, map_input


def solution1(inp):
    """Solves the first part of the challenge"""
    groups = inp.split('\n\n')
    s = 0
    for group in groups:
        letters = set(group.replace("\n", ""))
        print(group, len(letters))
        s += len(letters)
    return s


def solution2(inp):
    """Solves the second part of the challenge"""
    groups = inp.split('\n\n')
    s = 0
    for group in groups:
        groupans = None
        for people in group.split('\n'):
            pansw = set(people)
            if groupans is None:
                groupans = pansw
            else:
                groupans = groupans.intersection(pansw)
        s += len(groupans)
    return s


if __name__ == "__main__":
    CURRENT_DAY = 6
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
