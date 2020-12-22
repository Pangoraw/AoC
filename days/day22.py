"""
Solution for day 22/12/2020
Created at 07:49:37 - 22/12/20
"""

import sys
sys.path.append("../aoc")
from functools import reduce
from copy import deepcopy

from aoc import challenge_runner
from aoc.parser import get_lines



def solution1(inp):
    """Solves the first part of the challenge"""
    pl1, pl2 = inp.strip().split("\n\n")

    deck1, deck2 = [], []
    for c1 in pl1.split("\n")[1:]:
        deck1.append(int(c1))
    for c2 in pl2.split("\n")[1:]:
        deck2.append(int(c2))

    while len(deck1) != 0 and len(deck2) != 0:
        c1, c2 = deck1.pop(0), deck2.pop(0)

        if c1 > c2:
            deck1.append(max(c1, c2))
            deck1.append(min(c1, c2))
        else:
            deck2.append(max(c1, c2))
            deck2.append(min(c1, c2))

    winner = deck1 if len(deck1) != 0 else deck2
    return reduce(lambda x, y: x + (y[0]+1) * y[1], enumerate(winner[::-1]), 0)


def solution2(inp):
    """Solves the second part of the challenge"""
    pl1, pl2 = inp.strip().split("\n\n")

    deck1, deck2 = [], []
    for c1 in pl1.split("\n")[1:]:
        deck1.append(int(c1))
    for c2 in pl2.split("\n")[1:]:
        deck2.append(int(c2))

    def hash_round(deck1, deck2):
        return "".join(map(str, deck1)) + "|" + "".join(map(str, deck2))

    def subgame(deck1, deck2, j = 0):
        rounds = {}
        while len(deck1) != 0 and len(deck2) != 0:
            round_hash = hash_round(deck1, deck2)
            if round_hash in rounds:
                return True
            rounds[round_hash] = True
            c1, c2 = deck1.pop(0), deck2.pop(0)
            if len(deck1) + 1 > c1 and len(deck2) + 1 > c2:
                player1_wins = subgame(deepcopy(deck1[:c1]), deepcopy(deck2[:c2]), j+1)
                if player1_wins:
                    deck1.append(c1)
                    deck1.append(c2)
                else:
                    deck2.append(c2)
                    deck2.append(c1)
            elif c1 > c2:
                deck1.append(max(c1, c2))
                deck1.append(min(c1, c2))
            else:
                deck2.append(max(c1, c2))
                deck2.append(min(c1, c2))
        return len(deck1) != 0

    res = subgame(deck1, deck2)
    winner = deck1 if res else deck2
    return reduce(lambda x, y: x + (y[0]+1) * y[1], enumerate(winner[::-1]), 0)


if __name__ == "__main__":
    CURRENT_DAY = 22
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
