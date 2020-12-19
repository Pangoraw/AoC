"""
Solution for day 19/12/2020
Created at 09:10:35 - 19/12/20
"""

import sys
sys.path.append("../aoc")
from functools import lru_cache
from itertools import product

from aoc import challenge_runner
from aoc.parser import get_lines


def valid_count(inp, sol2=False):
    rules, messages = inp.strip().split("\n\n")
    rules = rules.split("\n")
    messages = messages.split("\n")
    rrules = {}
    for rule in rules:
        rrule = []
        n, r = rule.split(":")
        if r.count('"') == 2:
            rrule = r.strip()[1:-1]
        else:
            subrules = r.split("|")
            for sr in subrules:
                rrule.append(list(map(int, sr.strip().split(" "))))
        rrules[int(n)] = rrule
    N = 100
    for i in range(1, N):
        rrules[f"8_{i}"] = [[42] * i]
        rrules[f"11_{i}"] = [[42] * i + [31] * i]

    def match_rec():
        return False, 0

    @lru_cache()
    def match_str(match, rule):
        rule_def = rrules[rule]
        if len(match) == 0:
            return False, 0
        if isinstance(rule_def, str):
            assert(len(rule_def) == 1)
            return match[0] == rule_def, 1
        matches = set()
        for sr in rule_def:
            i = 0
            valid = True
            for r in sr:
                res, offset = match_str(match[i:], r)
                if res:
                    i += offset
                else:
                    valid = False
                    break
            if valid:
                if rule == 0 and i != len(match):
                    return False, i
                return True, i
        return False, 0

    def match2(match):
        for i, j in product(range(1, N), repeat=2):
            res, offset = match_str(match, f"8_{i}")
            if not res:
                continue
            res, new_offset = match_str(match[offset:], f"11_{j}")
            if res and offset + new_offset == len(match):
                return True
        return False

    if sol2:
        return sum(match2(msg) for msg in messages)
    return sum(match_str(msg, 0)[0] for msg in messages)


def solution1(inp):
    """Solves the first part of the challenge"""
    return valid_count(inp, False)

def solution2(inp):
    """Solves the second part of the challenge"""
    return valid_count(inp, True)


if __name__ == "__main__":
    CURRENT_DAY = 19
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
