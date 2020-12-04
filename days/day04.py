"""
Solution for day 04/12/2020
Created at 07:34:45 - 04/12/20
"""

import sys
sys.path.append("../aoc")
import re

from aoc import challenge_runner
from aoc.parser import get_lines, map_input

def is_pass_valid(passp, sol1=True):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passp = passp.replace("\n", " ").split(" ")
    keys_present = []
    values = []
    for val in passp:
        k, v = val.split(":")
        keys_present.append(k)
        values.append(v)
    for k, v in zip(keys_present, values):
        if k in keys:
            keys.remove(k)
            if sol1:
                continue
            if k == "byr":
                if 1920 > int(v) or int(v) > 2002:
                    return False
            elif k == "iyr":
                if 2010 > int(v) or int(v) > 2020:
                    return False
            elif k == "eyr":
                if 2020 > int(v) or int(v) > 2030:
                    return False
            elif k == "hgt":
                unit = v[-2:]
                if unit not in ["cm", "in"]:
                    return False

                size = int(v[:-2])
                if unit == "cm" and (150 > size or size > 193):
                    return False
                if unit == "in" and (59 > size or size > 76):
                    return False
            elif k == "hcl":
                if not re.match(r"^#(\d|[a-f]){6}$", v):
                    return False
            elif k == "ecl":
                if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    return False
            elif k == "pid":
                if not re.match(r"^\d{9}$", v):
                    return False

    return len(keys) == 0



def solution1(inp):
    """Solves the first part of the challenge"""
    s = 0
    for psp in inp.strip().split("\n\n"):
        if is_pass_valid(psp):
            s += 1
    return s


def solution2(inp):
    """Solves the second part of the challenge"""
    s = 0
    for psp in inp.strip().split("\n\n"):
        if is_pass_valid(psp, False):
            s += 1
    return s


if __name__ == "__main__":
    CURRENT_DAY = 4
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
