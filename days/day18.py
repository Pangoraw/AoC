"""
Solution for day 18/12/2020
Created at 07:54:43 - 18/12/20
"""

import sys
sys.path.append("../aoc")
import re

from aoc import challenge_runner
from aoc.parser import get_lines


def last_parens(equ):
    last = None
    for i, c in enumerate(equ):
        if c == ')':
            last = i
    return last


def eval(equ, top_level=False, sol2=False):
    i = 0
    s = None
    while i < len(equ):
        if equ[i] == '(':
            if s == None:
                s, o = eval(equ[i+1:last_parens(equ)])
                i += o
            i += 1
        elif equ[i] == '+':
            if equ[i+1] == '(':
                n, o = eval(equ[i+2:last_parens(equ)])
                o += 2
            else:
                n, o = (int(equ[i+1]), 2)
            s += n
            i += o
        elif equ[i] == '*':
            if equ[i+1] == '(':
                n, o = eval(equ[i+2:last_parens(equ)])
                o += 2
            else:
                n, o = (int(equ[i+1]), 2)
            s *= n
            i += o
        elif equ[i] == ')':
            if not top_level:
                return s, i + 1
            i += 1
        else:
            s = int(equ[i])
            i += 1
    return s, i + 1


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    return sum(map(lambda x: x[0], [eval(equ.replace(" ", ""), True) for equ in inp]))


def parenthesize(equ):
    new_equ = "(((("
    for i, c in enumerate(equ):
        if c == '(':
            new_equ = new_equ + '(((('
        elif c == ')':
            new_equ = new_equ + '))))'
        elif c == '+':
            new_equ = new_equ + ')+('
        elif c == '*':
            new_equ = new_equ + '))*(('
        else:
            new_equ += c
    new_equ += '))))'
    return new_equ


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    res = [eval(parenthesize(e.replace(" ", "")), True)[0] for e in inp]
    return sum(res)


if __name__ == "__main__":
    CURRENT_DAY = 18
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
