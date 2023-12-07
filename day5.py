import requests
from cookies import cookies
import re
import math

day = 5
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()

starts = {"red": 12, "green": 13, "blue": 14}

def get_next_val(map, val):
    for x in map:
        d, s, n = tuple(x)
        if int(s) <= int(val) < int(s) + n:
            return d + (int(val) - s)
    return val


def get_maps_and_edges(lines):
    i = 2
    maps = {}
    edges = {}
    while i < len(lines):
        source = lines[i].split()[0].split("-")[0]
        dest = lines[i].split()[0].split("-")[-1]
        edges[source] = edges.get(source, []) + [dest]
        i += 1
        while i < len(lines) and lines[i].strip():
            vals = lines[i].split()
            maps[(source, dest)] = sorted(maps.get((source, dest), []) + [[int(v) for v in vals]], key=lambda x: [x[1], x[0]])
            i += 1
        i += 1
    return maps, edges

def solve(seeds, lines, start="seed"):
    maps, edges = get_maps_and_edges(lines)
    min_val = None
    for seed in seeds:
        frontier = [(start, seed)]
        while frontier:
            source, val = frontier.pop(0)
            if source == 'location':
                if min_val is None:
                    min_val = val
                min_val = min(min_val, val)
            if source in edges:
                for edge in edges[source]:
                    next_val = int(get_next_val(maps[(source, edge)], val))
                    frontier.append((edge, next_val))
    return min_val

def solve1(lines):
    seeds = lines[0].split()[1:]
    print(solve(seeds, lines))
    return solve(seeds, lines)

def solve2(lines):
    seeds_ranges = lines[0].split()[1:]
    print(seeds_ranges)
    ranges = [(int(seeds_ranges[i*2]), int(seeds_ranges[i*2]) + int(seeds_ranges[i*2 + 1]), "seed") for i in range(len(seeds_ranges)//2)]
    min_val = None
    maps, edges = get_maps_and_edges(lines)
    while ranges:
        start_seed, end_seed, source = tuple(ranges.pop(0))
        if start_seed >= end_seed:
            print(start_seed, end_seed, source)
        if source == "location":
            if min_val is None:
                min_val = start_seed
            min_val = min(min_val, start_seed)
        else:
            if source == "humidity" and start_seed == 620098496:
                print('hello')
            dest = edges[source][0]
            for x in maps[(source, dest)]:
                d, s, m = tuple(x)
                n = end_seed - start_seed
                if start_seed < s:
                    ranges.append((start_seed, min(end_seed,s), dest))
                    start_seed = s
                if start_seed >= end_seed:
                    break
                if start_seed < s + m:
                    offset = start_seed - s
                    ranges.append((d + offset, min(d + offset + n, d + m), dest))
                    start_seed = min(end_seed, s + m)
                if start_seed >= end_seed:
                    break
            if start_seed < end_seed:
                ranges.append((start_seed, end_seed, dest))
    return min_val


part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
with open("test.txt", "r") as f:
    data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)

# 620098496
# 86282489
# 639605852
# 37979713