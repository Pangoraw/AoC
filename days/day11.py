"""
Solution for day 11/12/2020
Created at 09:33:01 - 11/12/20
"""

import sys
sys.path.append("../aoc")
from functools import reduce
import copy

from aoc import challenge_runner
from aoc.parser import get_lines


def adjacents(grid, x, y):
    h, w = len(grid), len(grid[0])

    if x < w - 1 and y < h - 1:
        br = grid[y+1][x+1]
    else:
        br = "."
    if x < w - 1 and y > 0:
        tr = grid[y-1][x+1]
    else:
        tr = "."
    if x > 0 and y > 0:
        tl = grid[y-1][x-1]
    else:
        tl = "."
    if x > 0 and y < h - 1:
        bl = grid[y+1][x-1]
    else:
        bl = "."
    if y > 0:
        top = grid[y-1][x]
    else:
        top = "."
    if y < h - 1:
        bottom = grid[y+1][x]
    else:
        bottom = "."
    if x < w - 1:
        left = grid[y][x+1]
    else:
        left = "."
    if x > 0:
        right = grid[y][x-1]
    else:
        right = "."
    # print(br, bl, tr, tl, top, bottom, left, right)
    return sum(c == "#" for c in [br, bl, tr, tl, top, bottom, left, right])

def adjacents2(inp, x, y):
    h, w = len(inp), len(inp[0])

    br, bl, tr, tl, top, bottom, left, right = [None] * 8
    i = 1
    while any(c == None for c in [br, bl, tr, tl, top, bottom, left, right]):
        if top == None and y - i < 0:
            top = False
        elif top == None:
            if inp[y - i][x] == "#":
                top = True
            elif inp[y - i][x] == "L":
                top = False
        if bottom == None and y + i >= h:
            bottom = False
        elif bottom == None:
            if inp[y + i][x] == "#":
                bottom = True
            elif inp[y + i][x] == "L":
                bottom = False
        if left == None and x - i < 0:
            left = False
        elif left == None:
            if inp[y][x - i] == "#":
                left = True
            elif inp[y][x - i] == "L":
                left = False
        if right == None and x + i >= w:
            right = False
        elif right == None:
            if inp[y][x + i] == "#":
                right = True
            elif inp[y][x + i] == "L":
                right = False
        if tl == None and (y - i < 0 or x - i < 0):
            tl = False
        elif tl == None:
            if inp[y - i][x - i] == "#":
                tl = True
            elif inp[y - i][x - i] == "L":
                tl = False
        if tr == None and (y - i < 0 or x + i >= w):
            tr = False
        elif tr == None:
            if inp[y - i][x + i] == "#":
                tr = True
            elif inp[y - i][x + i] == "L":
                tr = False
        if bl == None and (y + i >= h or x - i < 0):
            bl = False
        elif bl == None:
            if inp[y + i][x - i] == "#":
                bl = True
            elif inp[y + i][x - i] == "L":
                bl = False
        if br == None and (y + i >= h or x + i >= w):
            br = False
        elif br == None:
            if inp[y + i][x + i] == "#":
                br = True
            elif inp[y + i][x + i] == "L":
                br = False
        i += 1

    return sum([br, bl, tr, tl, top, bottom, left, right])

def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    for i, r in enumerate(inp):
        inp[i] = list(r)

    change = True
    i = 0
    while change:
        i += 1
        change = False
        new_grid = copy.deepcopy(inp)
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                if inp[y][x] == "L" and adjacents(inp, x, y) == 0:
                    new_grid[y][x] = "#"
                    change = True
                if inp[y][x] == "#" and adjacents(inp, x, y) >= 4:
                    new_grid[y][x] = "L"
                    change = True
        inp = new_grid

    return reduce(lambda acc, x: acc + sum([c == "#" for c in x]), inp, 0)

def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    for i, r in enumerate(inp):
        inp[i] = list(r)

    change = True
    i = 0
    while change:
        i += 1
        change = False
        new_grid = copy.deepcopy(inp)
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                if inp[y][x] == "L" and adjacents2(inp, x, y) == 0:
                    new_grid[y][x] = "#"
                    change = True
                if inp[y][x] == "#" and adjacents2(inp, x, y) >= 5:
                    new_grid[y][x] = "L"
                    change = True
        inp = new_grid

    return reduce(lambda acc, x: acc + sum([c == "#" for c in x]), inp, 0)

if __name__ == "__main__":
    CURRENT_DAY = 11
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
