import requests
from cookies import cookies
import re

day = 3
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()

starts = {"red": 12, "green": 13, "blue": 14}

def find_sum(lines):
    total = 0
    for line in lines:
        sofar = ""
        for char in line:
            if char.isdigit():
                sofar += char
            else:
                if sofar:
                    total += int(sofar)
                sofar = ""
        if sofar:
            total += int(sofar)    
    return total

def fill(grid, r, c):
    frontier = [(r+1,c), (r,c+1), (r+1,c+1), (r-1,c), (r,c-1), (r-1,c-1), (r+1,c-1), (r-1,c+1)]
    for x,y in frontier:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y].isdigit():
                grid[x] = grid[x][:y] + "." + grid[x][y+1:]
                left = y - 1
                right = y + 1
                while 0 <= left and grid[x][left].isdigit():
                    grid[x] = grid[x][:left] + "." + grid[x][left+1:]
                    left -= 1
                while right < len(grid[0]) and grid[x][right].isdigit():
                    grid[x] = grid[x][:right] + "." + grid[x][right+1:]
                    right += 1
    return grid

def solve1(lines):
    for i,x in enumerate(lines):
        lines[i] = x.strip()
    total = find_sum(lines)
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if not lines[r][c].isdigit() and lines[r][c] != ".":
                lines = fill(lines, r,c)
    not_include = find_sum(lines)
    return (total-not_include)

def get_gear(grid, r, c):
    frontier = [(r+1,c), (r,c+1), (r+1,c+1), (r-1,c), (r,c-1), (r-1,c-1), (r+1,c-1), (r-1,c+1)]
    vals = []
    explored = set()
    for x,y in frontier:
        if (x,y) not in explored:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y].isdigit():
                    left = y
                    while 0 <= left and grid[x][left].isdigit():
                        explored.add((x, left))
                        left -= 1
                    right = left
                    if (right != y and right >= 0) or right < 0:
                        right += 1
                    sofar = ""
                    while right < len(grid[0]) and grid[x][right].isdigit():
                        sofar += grid[x][right]
                        explored.add((x, right))
                        right += 1
                    if sofar:
                        vals.append(int(sofar))
    print(vals)
    if len(vals) == 2:
        print(vals)
        return vals[0]*vals[1]
    return 0

def solve2(lines):
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == '*':
                total += get_gear(lines,r,c)
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
