import requests
from cookies import cookies
import re
from math import gcd

day = 8
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()

starts = {"red": 12, "green": 13, "blue": 14}

def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -1*advantage % green_len
    )
    return -1*phase % period


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def lcm(a, b, offset):
    return arrow_alignment(a, b, offset)

def solve1(lines):
    directions = [i for i in lines[0].strip()]
    edges = {}
    start = "AAA"
    for i in range(2, len(lines)):
        if lines[i]:
            line = lines[i].split("=")
            left = line[0].strip()
            parts = line[1].strip()[1:-1].split(',')
            right = (parts[0].strip(), parts[1].strip())
            edges[left] = right
    ct = 0
    while start != 'ZZZ':
        l, r = edges[start]
        if directions[ct%len(directions)] == 'L':
            start = l
        else: 
            start = r
        ct += 1
    return ct

def solve2(lines):
    directions = [i for i in lines[0].strip()]
    edges = {}
    starts = []
    ends = []
    for i in range(2, len(lines)):
        if lines[i]:
            line = lines[i].split("=")
            left = line[0].strip()
            if left[-1] == "A":
                starts.append(left)
            if left[-1] == "Z":
                ends.append(left)
            parts = line[1].strip()[1:-1].split(',')
            right = (parts[0].strip(), parts[1].strip())
            edges[left] = right
    ct = 0
    cycles = []
    print(starts)
    for start in starts:
        explored = set()
        cycle = []
        ct = 0
        while (start, ct%len(directions)) not in explored:
            explored.add((start, ct))
            cycle.append(start)
            l, r = edges[start]
            if directions[ct%len(directions)] == 'L':
                start = l
            else: 
                start = r
            ct += 1
        full_cycle = cycle[ct%len(directions):]
        z = [i for i,x in enumerate(full_cycle) if x[-1] == "Z"][-1]
        cycles.append((ct%len(directions) + z, len(full_cycle)))
    print(cycles)
    ct = 0
    lowest_mult = 1
    for offset, length in cycles:
        lowest_mult = lcm(lowest_mult, length, offset)
    return lowest_mult
part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
# with open("test.txt", "r") as f:
#     data = f.readlines()
part2 += solve2(data)
        
print(part1)
print(part2)
