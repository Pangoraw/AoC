"""
Solution for day 14/12/2020
Created at 08:07:21 - 14/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)

    one_mask = 0
    zero_mask = 0
    mem = {}

    for inst in inp:
        k, v = inst.split("=")
        if k.strip() == "mask":
            one_mask = 0
            zero_mask = 0
            v = v.strip()
            assert len(v) == 36
            for i, c in enumerate(v):
                if c == "0":
                    zero_mask |= 1 << (36 - i - 1)
                elif c == "1":
                    one_mask |= 1 << (36 - i - 1)
                elif c == "X":
                    continue
                else:
                    raise Exception(f"Unknown char {c}")
            zero_mask = ~zero_mask
        else:
            loc = k.strip()[4:-1]
            v = int(v.strip())
            mem[loc] = (v | one_mask) & zero_mask

    return sum(v for v in mem.values())
        

def gen_addresses(address):
    for i, c in enumerate(address):
        if c == "X":
            sequel = gen_addresses(address[i+1:])
            return [address[:i] + "0" + add for add in sequel] + [address[:i] + "1" + add for add in sequel]
    return [address]


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)

    mem = {}
    for inst in inp:
        k, v = inst.split("=")
        if k.strip() == "mask":
            current_mask = v.strip()
        else:
            loc = bin(int(k.strip()[4:-1]))[2:]
            loc = "0" * (len(current_mask) - len(loc)) + loc
            v = int(v.strip())
            for i, c in enumerate(current_mask):
                if c == "1":
                    loc = loc[:i] + "1" + loc[i+1:]
                elif c == "X":
                    loc = loc[:i] + "X" + loc[i+1:]
            addresses = gen_addresses(loc)
            for add in addresses:
                mem[int(add, 2)] = v

    return sum(v for v in mem.values())


if __name__ == "__main__":
    CURRENT_DAY = 14
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
