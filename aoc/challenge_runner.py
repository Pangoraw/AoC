"""
Runs the two solutions against the input
"""

import argparse

from aoc import challenge_input


def run_for_day(day, solution1, solution2):
    """Runs the solution with the input for the day"""
    input_value = challenge_input.get_input_for_day(day)
    run(input_value, solution1, solution2)


def run(input_value, solution1, solution2):
    """Runs one of the two solution"""
    run1, run2 = parse_args()

    if run1:
        result1 = solution1(input_value)
        print(f"Solution 1 = {result1}")

    if run2:
        result2 = solution2(input_value)
        print(f"Solution 2 = {result2}")


def parse_args():
    """
    Parse command line arguments to determine wether or not to run
    solution1 and 2
    """
    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument(
        '-D',
        action="store_true",
        help="Whether or not to run solution 2 and skip solution 1",
    )

    args = parser.parse_args()
    return (not args.D), args.D
