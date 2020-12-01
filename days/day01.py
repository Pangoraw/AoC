"""
Solution for day  1/12/2020
Created at 08:41:12 - 01/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner

CURRENT_DAY = 1


def solution1(inp):
    """Solves the first part of the challenge"""
    parse_inp = [int(n) for n in inp.split('\n') if len(n) > 0]

    for x in parse_inp:
        for y in parse_inp:
            if x + y == 2020:
                return x * y


def solution2(inp):
    """Solves the first part of the challenge"""
    parse_inp = [int(n) for n in inp.split('\n') if len(n) > 0]

    for x in parse_inp:
        for y in parse_inp:
            for z in parse_inp:
                if x + y + z == 2020:
                    return x * y * z


if __name__ == "__main__":
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
