"""
Solution for day 02/12/2020
Created at 08:11:00 - 02/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner


def count_letter(string, ch):
    s = 0
    for c in string:
        if c == ch:
            s += 1
    return s


def is_pwd_valid(pwd):
    splits = pwd.split(':')
    constraint = splits[0]
    password = splits[1]

    ch = constraint[-1]
    print(constraint[:-2].split('-'))
    a, b = constraint[:-2].split('-')
    a = int(a)
    b = int(b)

    N = count_letter(password, ch)
    return N >= a and N <= b


def solution1(inp):
    """Solves the first part of the challenge"""
    pwds = [s for s in inp.split('\n') if len(s) > 0]

    s = 0
    for pwd in pwds:
        if is_pwd_valid(pwd):
            s += 1
    return s


def is_pwd_valid2(pwd):
    splits = pwd.split(':')
    constraint = splits[0]
    password = splits[1]
    print('"', password[1:], '"')

    ch = constraint[-1]
    a, b = constraint[:-2].split('-')
    a = int(a)
    b = int(b)

    return (password[a] == ch) ^ (password[b] == ch)


def solution2(inp):
    """Solves the second part of the challenge"""
    pwds = [s for s in inp.split('\n') if len(s) > 0]
    s = 0
    for pwd in pwds:
        if is_pwd_valid2(pwd):
            s += 1
    return s


if __name__ == "__main__":
    CURRENT_DAY = 2
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
