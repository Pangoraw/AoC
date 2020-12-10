"""
Solution for day 08/12/2020
Created at 07:28:01 - 08/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines


class Prg:
    def __init__(self, instrs):
        self.instrs = instrs
        self.pc = 0
        self.visited = set()
        self.reg = 0

    def step(self):
        if self.pc in self.visited:
            return self.reg
        self.visited.add(self.pc)

        instr = self.instrs[self.pc]
        inst, v = instr.split(" ")

        if inst == "acc":
            self.reg += int(v)
            self.pc += 1
        elif inst == "nop":
            self.pc += 1
        elif inst == "jmp":
            self.pc += int(v)

        if self.pc == len(self.instrs):
            return self.reg
        return None

    def run(self):
        val = self.step()
        while val == None:
            val = self.step()
        return val, self.pc == len(self.instrs)


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    prg = Prg(inp)
    acc, _ = prg.run()
    return acc


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    done = False

    cur_idx = next(
        i for i, inst in enumerate(inp)
        if "jmp" in inst or "nop" in inst)
    cid = 0
    while not done:
        if "jmp" in inp[cur_idx]:
            inp[cur_idx] = inp[cur_idx].replace("jmp", "nop")
        elif "nop" in inp[cur_idx]:
            inp[cur_idx] = inp[cur_idx].replace("nop", "jmp")

        prg = Prg(inp)
        acc, done = prg.run()

        if "jmp" in inp[cur_idx]:
            inp[cur_idx] = inp[cur_idx].replace("jmp", "nop")
        elif "nop" in inp[cur_idx]:
            inp[cur_idx] = inp[cur_idx].replace("nop", "jmp")

        cur_idx = next(
            i + cur_idx + 1 for i, inst in enumerate(inp[cur_idx+1:])
            if "jmp" in inst or "nop" in inst)

    return acc


if __name__ == "__main__":
    CURRENT_DAY = 8
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
