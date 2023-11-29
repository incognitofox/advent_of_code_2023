import requests
from cookies import cookies
import re

day = 2
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

starts = {"red": 12, "green": 13, "blue": 14}

def solve1(line):
    data = line.split(":")
    rounds = data[1].split(";")
    for round in rounds:
        counts = {"red": 0, "green":0, "blue":0}
        round = round.strip()
        colors = round.split(",")
        for color in colors:
            color = color.strip()
            vals = color.split()
            counts[vals[1]] += int(vals[0])
            if counts[vals[1]] >  starts[vals[1]]:
                return 0
    return int(data[0].split()[-1])

def solve2(line):
    data = line.split(":")
    rounds = data[1].split(";")
    counts = {"red": 0, "green":0, "blue":0}
    for round in rounds:
        round = round.strip()
        colors = round.split(",")
        for color in colors:
            color = color.strip()
            vals = color.split()
            counts[vals[1]] = max(counts[vals[1]], int(vals[0]))
    return counts["red"]*counts['green']*counts['blue']

part1 = 0
part2 = 0
for line in data:
    if line:
        part1 += solve1(line)
        part2 += solve2(line)
        
print(part1)
print(part2)