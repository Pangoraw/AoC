"""
Solution for day 13/12/2020
Created at 10:49:08 - 13/12/20
"""

import sys
sys.path.append("../aoc")

from tqdm import tqdm

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    earliest = int(inp[0])
    notes = inp[1].split(',')
    min_bus = None
    for bus in notes:
        if bus == 'x':
            continue
        bus = int(bus)
        wait_time = bus - earliest % bus
        if min_bus == None or wait_time < (min_bus - earliest % min_bus):
            min_bus = bus
    return min_bus * (min_bus - earliest % min_bus)


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    notes = inp[1].split(",")

    offsets = {}
    for i, bus in enumerate(notes):
        if bus == 'x':
            continue
        bus = int(bus)
        offsets[bus] = i
    buses = set(offsets)
    old_buses = buses.copy()

    def search(bus, offset, t):
        if (t + offset) % bus == 0:
            buses.remove(bus)
            if len(buses) == 0:
                return True
            new_bus = max(buses)
            return search(new_bus, offsets[new_bus], t)
        return False

    cbus = max(buses)
    max_bus = cbus
    s = 100_000_000_000_000
    s = 0
    s = s - s % cbus - offsets[cbus]
    delta = cbus
    stack = buses.copy()
    stack.remove(cbus)
    sec_max = max(stack)
    while not search(max_bus, offsets[max_bus], offsets[max_bus]):
        buses = old_buses.copy()
        s += delta
        if (s + offsets[sec_max]) % sec_max == 0:
            if len(stack) != 0:
                cbus = max(stack)
                stack.remove(cbus)
                if len(stack) != 0:
                    sec_max = max(stack)
                else:
                    return s
                delta *= cbus

    return s - offsets[max(offsets)]


if __name__ == "__main__":
    CURRENT_DAY = 13
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
