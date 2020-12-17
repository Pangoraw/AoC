"""
Solution for day 17/12/2020
Created at 09:08:32 - 17/12/20
"""

import sys
sys.path.append("../aoc")
from itertools import product

import numpy as np

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    W = len(inp) + 7 * 2
    mid = W // 2
    start = mid - len(inp) // 2
    mat = np.zeros((W, W, W), dtype=int)
    start_mat = np.zeros((len(inp), len(inp[0])), dtype=int)
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            start_mat[y, x] = 0 if c == "." else 1
    mat[start:start+len(inp), start:start+len(inp), mid] = start_mat
    new_mat = np.zeros((W, W, W), dtype=int)
    for i in range(6):
        for x, y, z in product(range(1, W - 1), repeat=3):
            n_neighbors = np.sum(mat[y-1:y+2, x-1:x+2, z-1:z+2]) - mat[y, x, z]
            if mat[y, x, z] == 0 and n_neighbors == 3:
                new_mat[y, x, z] = 1
            elif mat[y, x, z] == 1 and n_neighbors in [2, 3]:
                new_mat[y, x, z] = 1
        mat = new_mat
        new_mat = np.zeros((W, W, W), dtype=int)
    return np.sum(mat)


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    W = len(inp) + 7 * 2
    mid = W // 2
    start = mid - len(inp) // 2
    mat = np.zeros((W, W, W, W), dtype=int)
    start_mat = np.zeros((len(inp), len(inp[0])), dtype=int)
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            start_mat[y, x] = 0 if c == "." else 1
    mat[start:start+len(inp), start:start+len(inp), mid, mid] = start_mat
    new_mat = np.zeros((W, W, W, W), dtype=int)
    for i in range(6):
        for x, y, z, w in product(range(1, mat.shape[0] - 1), repeat=4):
            n_neighbors = np.sum(mat[y-1:y+2, x-1:x+2, z-1:z+2, w-1:w+2]) - mat[y, x, z, w]
            if mat[y, x, z, w] == 0 and n_neighbors == 3:
                new_mat[y, x, z, w] = 1
            elif mat[y, x, z, w] == 1 and n_neighbors in [2, 3]:
                new_mat[y, x, z, w] = 1
        mat = new_mat
        new_mat = np.zeros((W, W, W, W), dtype=int)
    return np.sum(mat)


if __name__ == "__main__":
    CURRENT_DAY = 17
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
