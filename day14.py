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

def solve1(lines):
    total = 0
    col_maxes = {i: 0 for i in range(len(lines[0]))}
    print("last", lines[-1])
    lines = lines[:-1]
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "#":
                col_maxes[c] = r+1
            if ch == "O":
                total += (len(lines) - col_maxes[c])
                col_maxes[c] += 1
    return total

def tilt_up(lines):
    new_lines = []
    for r, line in enumerate(lines):
        row = []
        for c, ch in enumerate(line):
            next_char = ch
            if ch == "#":
                col_maxes[c] = r+1
            if ch == "O":
                total += (len(lines) - col_maxes[c])
                col_maxes[c] += 1
                next_char = "."
            row.append(next_ch)
        new_lines.append(row)

def solve2(lines):

    return 0

part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
# with open("test.txt", "r") as f:
#     data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
