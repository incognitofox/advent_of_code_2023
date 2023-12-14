import requests
from cookies import cookies
import re
import bisect

day = 13
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

with open("test.txt", "r") as f:
    data = f.readlines()

def find_symmetry(line):
    centers = set()
    for i in range(1,len(line)):
        #print(i, "forward:", line[:i][::-1][:min(i, min(2*i+1, len(line)) - i)], line[i: min(2*i, len(line))])
        if line[:i][::-1][:min(i, min(2*i+1, len(line)) - i)] == line[i: min(2*i, len(line))]:
            centers.add(i)
    return centers

def get_symmetries(block, smudge=None, old_v=set(), old_h=set()):
    print(old_h, old_v)
    if smudge is not None:
        r,c = smudge
        print(r,c)
        val = '#'
        if block[r][c] == "#":
            val = '.'
        block[r] = block[r][:c] + val + block[r][c+1:]
        print(block)
    total = 0
    verticaL_symmetries = set([i for i in range(len(block[0]))])
    cols = [[row[i] for row in block] for i in range(len(block[0]))]
    for row in block:
        verticaL_symmetries = verticaL_symmetries.intersection(find_symmetry(row))
    print("vert:", verticaL_symmetries)
    for val in  verticaL_symmetries:
        if val not in old_v:
            total += val
    horizontal_symmetries = set([i for i in range(len(block))])
    for col in cols:
        horizontal_symmetries = horizontal_symmetries.intersection(find_symmetry(col))
    print("hor:", horizontal_symmetries)
    for val in horizontal_symmetries:
        if val not in old_h:
            total += val*100
    if smudge is not None:
        r,c = smudge
        val = '#'
        if block[r][c] == "#":
            val = '.'
        block[r] = block[r][:c] + val + block[r][c+1:]
    print("total:", total)
    return total, verticaL_symmetries, horizontal_symmetries
def solve1(lines):
    total = 0
    block = []
    for line in lines:
        line = line.strip()
        if line:
            block.append(line)
        else:
            total += get_symmetries(block)[0]
            block = []
    return total

def solve2(lines):
    total = 0
    block = []
    for line in lines:
        line = line.strip()
        if line:
            block.append(line)
        else:
            found = False
            _, v, h = get_symmetries(block)
            #print("old", v, h)
            for r in range(len(block)):
                for c in range(len(block[0])):
                    val, _, _ = get_symmetries(block, (r,c), v, h)
                    if val > 0:
                        total += val
                        found = True
                        print(r,c)
                        break
                if found:
                    #print(r, c)
                    break
            block = []
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
