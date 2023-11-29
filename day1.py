import requests
from cookies import cookies
import re

day = 1
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

def find_first_num(line, factor, nums={}):
    sofar = ""
    for c in line[::factor]:
        sofar += c
        if c.isdigit():
            return c
        for d in nums:
            if d[::factor] in sofar:
                return str(nums[d])
    return "0"

part1 = 0
part2 = 0
for line in data:
    if line:
        part1 += int(find_first_num(line, 1) + find_first_num(line, -1))
        part2 += int(find_first_num(line, 1, nums) + find_first_num(line, -1, nums))
print(part1)
print(part2)