import requests
from cookies import cookies
import re
import bisect

day = 14
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()

def tiltLeft(lines):
    lines = [[line[i] for line in lines] for i in range(len(lines[0]))]
    lines = tiltUp(lines)
    return [[line[i] for line in lines] for i in range(len(lines[0]))]

def tiltRight(lines):
    lines = [[line[i] for line in lines] for i in range(len(lines[0]))]
    lines = tiltDown(lines)
    return [[line[i] for line in lines] for i in range(len(lines[0]))]

def tiltDown(lines):
    new_lines = [[c for c in line] for line in lines]
    col_maxes = {i: 0 for i in range(len(lines[0]))}
    for r, line in enumerate(lines[::-1]):
        for c, ch in enumerate(line):
            if ch == "#":
                col_maxes[c] = r+1  
            if ch == "O":
                new_lines[-r-1][c] = "."
                new_lines[-col_maxes[c]-1][c] = "O"
                col_maxes[c] += 1
    return new_lines

def tiltUp(lines):
    new_lines = [[c for c in line] for line in lines]
    col_maxes = {i: 0 for i in range(len(lines[0]))}
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "#":
                col_maxes[c] = r+1  
            if ch == "O":
                new_lines[r][c] = "."
                new_lines[col_maxes[c]][c] = "O"
                col_maxes[c] += 1
    return new_lines

def score(lines):
    total = 0
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "O":
                total += (len(lines) - r)
    return total

def solve1(lines):
    lines = [line for line in lines if line]
    return score(tiltUp(lines))

def tuplify(lines):
    return tuple([tuple(line) for line in lines])

def solve2(lines):
    lines = [line.strip() for line in lines if line]
    explored = {}
    tilts = [lambda x: tiltUp(x), lambda x: tiltLeft(x), lambda x: tiltDown(x), lambda x: tiltRight(x)]
    ct = 0
    cycle = []
    i = 0
    while (tuplify(lines), ct) not in explored:
        explored[(tuplify(lines), ct)] = i
        cycle.append(lines.copy())
        lines = tilts[ct](lines)
        i += 1
        ct = (ct+1)%4
    val = explored[(tuplify(lines), ct)]
    cycle = cycle[val:]
    return score(cycle[(4*1000000000-val)%len(cycle)])

part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
# with open("test.txt", "r") as f:
#     data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
