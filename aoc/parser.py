"""
Functions useful for input parsing
"""


def get_lines(inp):
    """
    Splits input values into an array of strings
    """
    return inp.strip().split('\n')


def map_input(inp, func):
    """
    Map input strings through f
    """
    return map(func, get_lines(inp))
