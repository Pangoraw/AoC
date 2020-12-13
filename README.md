# Advent of Code :santa:

Repository for the Advent of Code 2020 in Python :snake:

## What did I learn?

Advent of Code is a good way to learn tips about the language you are using. Here is some of the things I learnt during advent 2020.

### Day 1

```python
from itertools import combinations

list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```

### Day 2

```python
"aaabbb".count("a") # 3
```

### Day 10

```python
from functools import lru_cache

@lru_cache(max_size=32)
def func(a):
  return a ** 100 # Costly calculation
```

### Day 11

```python
if x in range(w): # range implements __contains__
  grid[x] # sure to be valid
```

### Day 12

Raise an exception at the end of a `if/elif` chain to unmatched inputs to slip through (I wrote `O` instead of `W` initially). There is also native support for complex numbers in Python (`1j ** 2 = (-1 + 0j)`) !


### Day 13

[Chinese Remainder Theorem (CRT)](https://en.wikipedia.org/wiki/Chinese_remainder_theorem).

## Usage

The repository handles the download of input files automatically and caches them in the `inputs` folder to prevent server spam. The file [`day00.py`](https://github.com/Pangoraw/AoC/blob/main/days/day00.py) is used as a template for everyday. The `aoc` folder contains functions useful in common situations.

Every day, run the following command to bootstrap the file and download the corresponding input.

```
./new_day.sh
```

When the solution for the first part has been submitted you can run only part two by running:

```
./new_day.sh -D
```
