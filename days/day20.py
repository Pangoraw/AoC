"""
Solution for day 20/12/2020
Created at 08:42:20 - 20/12/20
"""

import sys
sys.path.append("../aoc")
import math
from itertools import product

import numpy as np

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = inp.strip().split("\n\n")
    W = int(math.sqrt(len(inp)))
    images = {}
    tiles = {}
    puzzle = []
    for t in inp:
        lines = t.split("\n")
        id = int(lines[0].split(" ")[1][:-1])
        lines = lines[1:]
        t, l, b, r = [], [], [], []
        for i in range(len(lines)):
            t.append(lines[0][i])
            l.append(lines[i][0])
            b.append(lines[-1][i])
            r.append(lines[i][-1])
        img = np.zeros((len(lines), len(lines)), dtype=int)
        for x, y in product(range(len(lines)), repeat=2):
            img[y, x] = 0 if lines[y][x] == '.' else 1
        images[id] = img
        tiles[id] = ["".join(t), "".join(l), "".join(b), "".join(r)]

    def flip(t):
        t, l, b, r = t
        return [l, t, r, b]

    def rotate(t):
        t, l, b, r = t
        return [r, t[::-1], l, b[::-1]]

    for x, t in tiles.items():
        s = 0
        matched_i = []
        for y, t2 in tiles.items():
            if x == y:
                continue
            for i, a in enumerate(t):
                for b in t2:
                    if a == b or a[::-1] == b:
                        matched_i.append(i)
                        s += 1
        if len(matched_i) == 2 and len(puzzle) == 0:
            while 1 in matched_i or 0 in matched_i:
                tiles[x] = rotate(tiles[x])
                images[x] = np.rot90(images[x])
                matched_i = list(map(lambda x: (x + 1) % 4, matched_i))
            puzzle.append([x])
            break

    explored = set(i for j in puzzle for i in j)
    for k in range(W):
        for i in range(1, W):
            src = puzzle[k][i-1]
            s = 0
            a = tiles[src][3]
            found = False
            while True:
                for y, t2 in tiles.items():
                    if y in explored:
                        continue
                    img = images[y].copy()
                    for j in range(8):
                        if j == 4:
                            t2 = flip(t2)
                            img = img.T
                        t2 = rotate(t2)
                        img = np.rot90(img)
                        b = t2[1]
                        if a == b:
                            puzzle[k].append(y)
                            explored.add(y)
                            images[y] = img
                            tiles[y] = t2
                            found = True
                            break
                if found:
                    break
                tiles[src] = rotate(rotate(rotate(flip(tiles[src]))))
                images[src] = np.rot90(np.rot90(np.rot90(images[src].T)))
                a = tiles[src][3]
        src = puzzle[k][0]
        a = tiles[src][2]
        found = False
        for y, t2 in tiles.items():
            if y in explored:
                continue
            img = images[y].copy()
            for j in range(8):
                if j == 4:
                    t2 = flip(t2)
                    img = img.T
                t2 = rotate(t2)
                img = np.rot90(img)
                b = t2[0]
                if a == b:
                    puzzle.append([y])
                    explored.add(y)
                    tiles[y] = t2
                    images[y] = img
                    break

    first = puzzle[0][0]
    image = np.zeros((W * (len(tiles[first][0]) - 2), W * (len(tiles[first][0]) - 2)), dtype=int)
    n_image = np.zeros((W * len(tiles[first][0]), W * len(tiles[first][0])), dtype=int)

    for x, y in product(range(len(puzzle)), repeat=2):
        id = puzzle[y][x]
        img = images[id]
        w = img.shape[0] - 2
        h = img.shape[0]
        image[y*w:(y+1)*w, x*w:(x+1)*w] = img[1:-1, 1:-1]
        n_image[y*h:(y+1)*h, x*h:(x+1)*h] = img
    mask = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    ], dtype=int)
    neg_mask = np.abs(mask - 1)
    Y = image.shape[0] - mask.shape[0]
    X = image.shape[1] - mask.shape[1]
    n_pixels = np.sum(mask)
    mh, mw = mask.shape

    match = False
    i = 0
    while i != 8:
        if i % 4 == 0:
            image = image.T
        i += 1
        image = np.rot90(image)
        for x in range(X):
            for y in range(Y):
                n_match = np.sum(image[y:y+mh, x:x+mw] * mask)
                if n_match == n_pixels:
                    match = True
                    image[y:y+mh, x:x+mw] *= neg_mask
        if match:
            break

    print("part1: ", puzzle[0][0] * puzzle[0][-1] * puzzle[-1][0] * puzzle[-1][-1])
    return np.sum(image)


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)


if __name__ == "__main__":
    CURRENT_DAY = 20
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
