"""
Solution for day 24/12/2020
Created at 08:55:21 - 24/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines


dirs = [("sw", [-1, 1]), ("se", [0, 1]),
        ("e",  [1, 0]), ("w", [-1, 0]),
        ("nw", [0, -1]),("ne",[1, -1])]


def build_tiles(inp):
    inp = get_lines(inp)
    tiles = {}
    for l in inp:
        x, y = 0, 0
        while len(l) > 0:
            for d in dirs:
                if l.startswith(d[0]):
                    dx, dy = d[1]
                    y += dy
                    x += dx
                    l = l[len(d[0]):]
                    break
        coords = f"{x},{y}"
        if coords not in tiles:
            tiles[coords] = True
        else:
            tiles[coords] = not tiles[coords]
    return tiles


def solution1(inp):
    """Solves the first part of the challenge"""
    return sum(build_tiles(inp).values())


def solution2(inp):
    """Solves the second part of the challenge"""
    tiles = build_tiles(inp)

    print("Day 0: ", sum(tiles.values()))
    for i in range(100):
        new_tiles = {}
        for x in range(-100, 100):
            for y in range(-100, 100):
                s = 0
                for d in dirs:
                    dx, dy = d[1]
                    coords = f"{x+dx},{y+dy}"
                    if coords in tiles:
                        s += int(tiles[coords])
                coords = f"{x},{y}"
                if coords in tiles and tiles[coords] and (s == 0 or s > 2):
                    new_tiles[coords] = False
                elif s == 2  and ((coords in tiles and not tiles[coords]) or coords not in tiles):
                    new_tiles[coords] = True
                elif coords in tiles:
                    new_tiles[coords] = tiles[coords]
        tiles = new_tiles
        print(f"Day {i+1}: ", sum(tiles.values()))

    return sum(tiles.values())


if __name__ == "__main__":
    CURRENT_DAY = 24
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
