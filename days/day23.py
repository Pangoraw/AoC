"""
Solution for day 23/12/2020
Created at 11:20:45 - 23/12/20
"""

import sys
sys.path.append("../aoc")
from tqdm import tqdm

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = list(map(int, inp.strip()))

    N_MOVES = 100
    i = 0
    cur_cup = 0
    while i < N_MOVES:
        print(i+1,inp)
        if cur_cup + 4 >= len(inp):
            tmp_hold = inp[cur_cup + 1:] + inp[:(cur_cup+4) % len(inp)]
            dc = (cur_cup+4) % len(inp)
            inp = inp[(cur_cup+4) % len(inp):cur_cup+1]
            cur_cup -= dc
        else:
            tmp_hold = inp[cur_cup + 1:cur_cup+4]
            inp = inp[:cur_cup + 1] + inp[(cur_cup + 4):]
        next_label = inp[cur_cup] - 1
        candidates = sorted(inp)
        print(candidates, next_label)
        while next_label not in candidates:
            next_label = next_label - 1
            if next_label <= 0:
                next_label = candidates[-1]
        print(tmp_hold, inp, next_label)
        next_index = inp.index(next_label)
        inp = inp[:next_index+1] + tmp_hold + inp[next_index+1:]
        if next_index < cur_cup:
            cur_cup = (cur_cup + 4) % len(inp)
        else:
            cur_cup = (cur_cup + 1) % len(inp)
        i += 1

    one_idx = inp.index(1)
    inp = inp[one_idx+1:] + inp[:one_idx]

    return "".join(map(str, inp))


def solution2(inp):
    """Solves the second part of the challenge"""
    return "in day23.cc"


if __name__ == "__main__":
    CURRENT_DAY = 23
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
