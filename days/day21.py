"""
Solution for day 21/12/2020
Created at 08:13:48 - 21/12/20
"""

import sys
sys.path.append("../aoc")

from aoc import challenge_runner
from aoc.parser import get_lines


def solution1(inp):
    """Solves the first part of the challenge"""
    inp = get_lines(inp)
    candidates = {}
    ing = []
    for recipe in inp:
        ingredients, allergens = recipe.split('(')
        ingredients = ingredients.strip().split(' ')
        allergens = allergens.strip()[9:-1].split(', ')
        for a in allergens:
            if a in candidates:
                candidates[a] = candidates[a].intersection(ingredients)
            else:
                candidates[a] = set(ingredients)
        ing += ingredients
    s = 0
    for i in ing:
        allergen = False
        for a in candidates:
            if i in candidates[a]:
                allergen = True
                break
        if not allergen:
            s += 1
    return s


def solution2(inp):
    """Solves the second part of the challenge"""
    inp = get_lines(inp)
    candidates = {}
    ing = []
    for recipe in inp:
        ingredients, allergens = recipe.split('(')
        ingredients = ingredients.strip().split(' ')
        allergens = allergens.strip()[9:-1].split(', ')
        for a in allergens:
            if a in candidates:
                candidates[a] = candidates[a].intersection(ingredients)
            else:
                candidates[a] = set(ingredients)
        ing += ingredients
    for i in ing:
        allergen = False
        for a in candidates:
            if i in candidates[a]:
                allergen = True
                break
        if not allergen:
            for a in candidates:
                if i in candidates[a]:
                    candidates[a].remove(i)
    stack = list(candidates.items())
    def resolve(j, avail):
        f, cand = stack[j]
        for i in avail.intersection(cand):
            if len(avail) == 1:
                return [i]
            avail.remove(i)
            res = resolve(j + 1, avail)
            avail.add(i)
            if res is not False:
                return [i] + res
        return False

    def is_allergen(x):
        for a in candidates:
            if x in candidates[a]:
                return True
        return False

    ing = filter(is_allergen, ing)
    avail = set(ing)
    names = list(map(lambda x: x[0], stack))
    return ",".join(map(lambda x: x[0], sorted(zip(resolve(0, avail), names), key=lambda x: x[1])))


if __name__ == "__main__":
    CURRENT_DAY = 21
    challenge_runner.run_for_day(CURRENT_DAY, solution1, solution2)
