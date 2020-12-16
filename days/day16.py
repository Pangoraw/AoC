"""
Solution for day 16/12/2020
Created at 07:40:52 - 16/12/20
"""

import sys
sys.path.append("../aoc")
from functools import reduce

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    rules, _, nearby = inp.strip().split("\n\n")
    rules = rules.split("\n")
    nearby = nearby.split("\n")[1:]

    rrules = []
    for rule in rules:
        a, b = rule.split(" or ")
        r1 = a.strip().split(" ")[-1]
        r2 = b.strip()
        def to_range(r):
            i, j = list(map(int, r.split("-")))
            return range(i, j + 1)
        rrules.append((to_range(r1), to_range(r2)))

    s = 0
    for ticket in nearby:
        ticket = list(map(int, ticket.split(",")))
        for v in ticket:
            valid = False
            for r in rrules:
                valid |= v in r[0] or v in r[1]
            if not valid:
                s += v
    return s


def solution2(inp):
    """Solves the second part of the challenge"""
    rules, mticket, nearby = inp.strip().split("\n\n")
    rules = rules.split("\n")
    nearby = nearby.split("\n")[1:]
    mticket = list(map(int, mticket.split("\n")[1].split(",")))
    rrules = []
    for rule in rules:
        a, b = rule.split(" or ")
        name = a.strip().split(":")[0]
        r1 = a.strip().split(" ")[-1]
        r2 = b.strip()
        def to_range(r):
            i, j = list(map(int, r.split("-")))
            return range(i, j + 1)
        rrules.append((to_range(r1), to_range(r2), name))

    nearby = [list(map(int, ticket.split(","))) for ticket in nearby]
    s = 0
    to_remove = []
    for i, ticket in enumerate(nearby):
        for v in ticket:
            valid = False
            for r in rrules:
                valid |= v in r[0] or v in r[1]
            if not valid:
                to_remove.append(i)
    nearby = list(map(lambda x: x[1], filter(lambda x: x[0] not in to_remove, enumerate(nearby))))
    indices = list(range(len(rrules)))
    keys = {}
    for rule in rrules:
        rule_idx = []
        for i in indices:
            if all(ticket[i] in rule[0] or ticket[i] in rule[1] for ticket in nearby):
                rule_idx.append(i)
        keys[rule[2]] = rule_idx

    stack = list(keys.items())
    def resolve(j, avail):
        f, cand = stack[j]
        for i in avail.intersection(cand):
            if len(avail) == 1:
                return [i]
            avail.remove(i)
            res = resolve(j + 1, avail)
            avail.add(i)
            if res != False:
                return [i] + res
        return False
    solver = resolve(0, set(range(len(rrules))))
    names = list(map(lambda x: x[0], stack))
    return reduce(lambda x, y: x * y, [mticket[v] for k, v in zip(names, solver) if k.startswith("departure")], 1)




if __name__ == "__main__":
    CURRENT_DAY = 16
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
