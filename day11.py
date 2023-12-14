import requests
from cookies import cookies
import re
import bisect

day = 11
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()


def solve1(lines):
    galaxies = []
    empty_rows = []
    full_cols = set()
    empty_cols = []
    for i, line in enumerate(lines):
        empty = True
        for j, c in enumerate(line):
            if c == '#':
                full_cols.add(j)
                empty = False
                galaxies.append((i,j))
        if empty:
            empty_rows.append(i)
    for i in range(len(lines[0])):
        if i not in full_cols:
            empty_cols.append(i)
    dist = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            r1, c1 = galaxies[i]
            r2, c2 = galaxies[j]
            rmax =  max(r1, r2)
            rmin = min(r1, r2)
            cmax = max(c1, c2)
            cmin = min(c1, c2)
            for k in range(rmin, rmax):
                if k in empty_rows:
                    dist += 999999
                dist += 1
            for k in range(cmin, cmax):
                if k in empty_cols:
                    dist += 999999
                dist += 1
        
    return dist

def solve2(lines):
    return 0


part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
with open("test.txt", "r") as f:
    data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
