import requests
from cookies import cookies
import re
import bisect

day = 12
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

with open("test.txt", "r") as f:
    data = f.readlines()

def check_valid(line, nums):
    groups = []
    curr = line[0]
    ct = 0
    for val in line:
        if val == curr:
            ct += 1
        else:
            groups.append((curr, ct))
            curr = val
            ct = 1
    groups.append((curr, ct))
    i = 0
    diff = True
    t = 0
    for c, ct in groups:
        if c == "#":
            t += 1
    for c, ct in groups:
        if c == "#":
            if i >= len(nums):
                return 1
            if nums[i] != ct:
                diff = False
            i += 1
    if diff and t == len(nums):
        return 0
    return 1

def get_num_arrangments(line, nums):
    frontier = [(line, 0)]
    ct = 0
    while frontier:
        #print(f"frontier: {frontier}")
        curr_line, start = frontier.pop(0)
        res = check_valid(curr_line, nums)
        if res == 0:
            # print(curr_line)
            ct += 1
        elif res > 0:
            for i in range(start, len(line)):
                if line[i] == "?":
                    frontier.append((curr_line[:i] + "#" + curr_line[i+1:], i+1))
    print(line, nums, ct)
    return ct

def solve1(lines):
    total = 0
    for line in lines:
        if line:
            left, right = tuple(line.split())
            nums = [int(i) for i in right.strip().split(",")]
            total += get_num_arrangments(left, nums)
    return total

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
