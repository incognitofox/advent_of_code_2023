import requests
from cookies import cookies
import re, math 

day = 6
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

with open("test.txt", "r") as f:
    data = f.readlines()

def solve1(lines):
    times = [int(i) for i in lines[0].split()[1:]]
    distances = [int(i) for i in lines[1].split()[1:]]
    total = 1
    for i, time in enumerate(times):
        count = 0
        for t in range(time):
            print(t*(time - t), distances[i])
            if t*(time - t) > distances[i]:
                count += 1
        total *= count
    return total

def solve2(lines):
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    count = 0
    for i in range(time):
        if i*(time - i) > distance:
            count += 1
    return count


part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
# with open("test.txt", "r") as f:
#     data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
