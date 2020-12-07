"""
Solution for day 07/12/2020
Created at 10:04:31 - 07/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines, map_input


class Bag:
    def __init__(self, color):
        self.color = color
        self.bags = {}
        self.counts = {}

    def add_bag(self, bag, count):
        self.bags[bag.color] = bag
        self.counts[bag.color] = count

    def visit(self, color, first=False):
        if not first and self.color == color:
            return 1
        return int(sum([self.bags[k].visit(color) for k in self.bags]) >= 1)

    def visit2(self):
        s = [self.bags[k].visit2() * self.counts[k] for k in self.bags]
        return sum(s) + 1


def build_bags(inp):
    bags = {}
    for bag in inp:
        color = bag.split('bags')[0].strip()
        if color not in bags:
            c_bag = Bag(color)
            bags[color] = c_bag
        else:
            c_bag = bags[color]
        contains = bag.strip().split('contain')[1].strip().split(',')
        for nbag in contains:
            if "no" in nbag.strip().split(" ")[0]:
                continue
            c = int(nbag.strip().split(" ")[0])
            col = nbag[len(str(c))+1:-4-(c > 1)].strip()
            if col not in bags:
                bags[col] = Bag(col)
            bags[color].add_bag(bags[col], c)
    return bags


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    bags = build_bags(inp)

    s = 0
    for k in bags:
        if k == 'shiny gold':
            continue
        s += bags[k].visit('shiny gold')

    print(bags['shiny gold'].visit('shiny gold', True))
    return s


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    bags = build_bags(inp)

    return bags['shiny gold'].visit2() - 1


if __name__ == "__main__":
    CURRENT_DAY = 7
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
