import requests
from cookies import cookies
import re

day = 10
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

with open("test.txt", "r") as f:
    data = f.readlines()

starts = {"red": 12, "green": 13, "blue": 14}

def get_next(mat, r, c, last, ct, path=[]):
    ds = {"|": (1, 0), "-":(0, 1), "L": (1, 1), "J": (1, -1), "F":(-1,1), "&": (-1,-1)}
    rhead = r - last[0]
    chead = c - last[1]
    if 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        if mat[r][c] == "S":
            mat[r][c] = 0
            return [(r+1, c, ct + 1, (r, c), path + [(r,c)]), (r, c+1, ct + 1, (r, c), path + [(r,c)]), (r-1, c, ct + 1, (r, c), path + [(r,c)]), (r, c-1, ct + 1, (r, c),  path + [(r,c)])]
        if mat[last[0]][last[1]] == 0:
            if mat[r][c] == "&" and not (rhead == 1 or chead == 1):
                return False
            if mat[r][c] == "|" and not (rhead == -1 or rhead == 1):
                return False
            if mat[r][c] == "-" and not (chead == -1 or chead == 1):
                return False
            if mat[r][c] == "L" and not (rhead == 1 or chead == -1):
                return False
            if mat[r][c] == "J" and not (rhead == 1 or chead == 1):
                return False
            if mat[r][c] == "F" and not (rhead == -1 or chead == -1):
                return False
        if mat[r][c] in ds:
            dr, dc = ds[mat[r][c]]
            if dr == 0 or dc == 0 and abs(rhead) == dr and abs(chead) == dc:
                return [(r + dr*rhead, c + dc*chead, ct + 1, (r, c), path + [(r,c)])]
            if rhead == dr:
                return [(r, c + dc, ct + 1, (r, c), path + [(r,c)])]
            if rhead == -1*dr:
                return [(r, c + dc*-1, ct + 1, (r, c), path + [(r,c)])]
            if chead == dc:            
                return [(r + dr, c, ct + 1, (r, c), path + [(r,c)])]
            if chead == -1*dc:
                return [(r + dr*-1 , c, ct + 1, (r, c), path + [(r,c)])]
    return False




def solve1(lines):
    mat = []
    s = ""
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line.strip()):
            if c == '7':
                c = '&'
            row.append(c)
            if c == "S":
                s = (i, j, 0, (i,j), [])
        mat.append(row)
    frontier = [(s)]
    max_ct = 0
    #print(mat)
    while frontier:
        #print()
        (r,c, ct, last, path) = frontier.pop(0)
        next = get_next(mat, r, c, last, ct)
        if next:
            frontier += next
            max_ct = max(max_ct, ct)
    for line in mat:
        print(line)
    print(len(mat), len(mat[0]))
    return max_ct

def find_zero(mat):
    max_ct = 0
    left = {'|','&','J'}
    right = {'L', '|', 'F'}
    up = {'-', 'J', 'L'}
    down = {'_', '&', 'F'}
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                frontier = [(r,c)]
                explored = set()
                ct = 0
                in_set = True
                while frontier:
                    r, c = frontier.pop(0)
                    if (r,c) not in explored and 0 <= r < len(mat) and 0 <= c < len(mat[0]):
                        explored.add((r,c))
                        if mat[r][c] == 0:
                            frontier += [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]
                            mat[r][c] = 8
                            ct += 1
                        if mat[r][c] in down and r + 1 < len(mat) and mat[r+1][c] in up:
                            in_set = False 
                        if mat[r][c] in up and r > 0 and mat[r-1][c] in down:
                            in_set = False
                        if mat[r][c] in left and c < len(mat) and mat[r][c+1] in right:
                            in_set = False
                        if mat[r][c] in right and c > 0 and mat[r][c-1] in left:
                            in_set = False
                if in_set:
                    max_ct += ct
    return mat, max_ct
def fill_edge(mat):
    nums = {0,1,2,8}
    left = {'|','&','J'}
    right = {'L', '|', 'F'}
    up = {'-', 'J', 'L'}
    down = {'_', '&', 'F'}
    frontier = []
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if r == 0 or c == 0 or r + 1 == len(mat) or c + 1 == len(mat[0]):
                dr = 1
                dc = 1
                if r + 1 == len(mat):
                    dr = -1
                if c + 1 == len(mat[0]):
                    dc = -1
                frontier.append((r,c,dr,dc))
    explored = set()
    while frontier:
        print(frontier)
        for line in mat:
            print(" ".join([str(i) for i in line]))
        r, c, dr, dc = frontier.pop(0)
        if (r,c) not in explored and 0 <= r < len(mat) and 0 <= c < len(mat[0]):
            explored.add((r,c))
            if mat[r][c] == 0:
                mat[r][c] = 2
                for d in [-1, 1]:
                    if 0 <= r + d < len(mat):
                        frontier.append((r+d, c, d, 0))
                    if 0 <= c + d < len(mat[0]) and mat[r][c + d] == 0:
                        frontier.append((r, c +d, 0, d))
            # else:
            #     if mat[r][c] in right and 0 < c and mat[r][c-1] not in (up | down) and dr != 0 and dc >= 0:
            #         frontier += [(r+1, c, 1, 1), (r-1, c, -1, 1)]
            #     if mat[r][c] in left and c  + 1 < len(mat[0]) and mat[r][c+1] not in (down | up) and dr != 0 and dc <= 0:
            #         frontier += [(r+1, c, 1, -1), (r-1, c, -1,-1)]
            #     if mat[r][c] in down and 0 < r and mat[r][c-1] not in (left | right) and dc != 0 and dr <= 0:
            #         frontier += [(r,c+1, -1, 1), (r,c-1,-1,-1)]
            #     if mat[r][c] in up and r + 1 < len(mat) and mat[r][c-1] not in (left | right) and dc != 0 and dr >= 0:
            #         frontier += [(r,c+1,1,1), (r,c-1,1,-1)]
    return mat

def solve2(lines):
    mat = []
    s = ""
    for i, line in enumerate(lines):
        if line:
            row = []
            for j, c in enumerate(line.strip()):
                if c == '7':
                    c = '&'
                row.append(c)
                if c == "S":
                    s = (i, j, 0, (i,j), [(i,j)])
            print(" ".join(row))
            mat.append(row)
    frontier = [(s)]
    max_ct = 0
    #print(mat)
    max_path = []
    explored = set()
    while frontier:
        #print()
        (r,c, ct, last, path) = frontier.pop(0)
        next = get_next(mat, r, c, last, ct, path)
        if next:
            explored.add((r,c))
            frontier += next
            max_ct = max(max_ct, ct)
            max_path = path
    max_path = set(max_path)
    for r, line in enumerate(mat):
        print(" ".join(['1' if (r,c) in max_path else '0' for c, _ in enumerate(line)]))
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                mat[r][c] = "S"
            if (r,c) not in explored:
                mat[r][c] = 0
    mat = fill_edge(mat)
    mat, max_ct = find_zero(mat)
    for line in mat:
        print(" ".join([str(i) for i in line]))
    return max_ct


part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
with open("test.txt", "r") as f:
    data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
