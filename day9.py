import requests
from cookies import cookies
import re
import math

day = 9
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

# with open("test.txt", "r") as f:
#     data = f.readlines()

def solve1(lines):
    total = 0 
    for line in lines:
        if line:
            values = [int(i) for i in line.split()]
            layers = [values]
            while any(values):
                new = []
                for i in range(1, len(values)):
                    new.append(values[i] - values[i-1])
                values = new
                layers.append(values)
            last = 0
            for layer in layers[::-1]:
                last = layer[-1] + last
            total += last
    return total

def solve2(lines):
    total = 0 
    for line in lines:
        if line:
            values = [int(i) for i in line.split()]
            layers = [values]
            while any(values):
                new = []
                for i in range(1, len(values)):
                    new.append(values[i] - values[i-1])
                values = new
                layers.append(values)
            last = 0
            for layer in layers[::-1]:
                last = layer[0] - last
            total += last
    return total


part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
# with open("test.txt", "r") as f:
#     data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
