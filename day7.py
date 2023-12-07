import functools
import requests
from cookies import cookies
import re
import math

day = 7
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()

starts = {"red": 12, "green": 13, "blue": 14}

def compare(tup1, tup2):
    hand1 = tup1[0]
    hand2 = tup2[0]
    card_val = {str(i+1): i+1 for i in range(10)}
    card_val['T'] = 10
    card_val['J'] = 0
    card_val['Q'] = 12
    card_val['K'] = 13
    card_val['A'] = 14
    freqs1 = {'J':0}
    freqs2 = {'J':0}
    for c in hand1:
        freqs1[c] = freqs1.get(c, 0) + 1
    for c in hand2:
        freqs2[c] = freqs2.get(c, 0) + 1
    order1 = sorted(freqs1.items(), key = lambda x: x[1], reverse=True)
    order1 = [x for x in order1 if x[0] != 'J']
    if not order1:
        order1 = [('J', 0)]
    j1 =  freqs1['J']
    order2 = sorted(freqs2.items(), key = lambda x: x[1], reverse=True)
    order2 = [x for x in order2 if x[0] != 'J']
    if not order2:
        order2 = [('J', 0)]
    j2 =  freqs2['J']
    order1[0] = (order1[0][0], order1[0][1] + j1)
    order2[0] = (order2[0][0], order2[0][1] + j2)
    if len(order1) == 1 and len(order2)==1:
        print(order1, order2)
    for i in range(len(order1)):
        if order1[i][1] > order2[i][1]:
            return 1
        if order1[i][1] < order2[i][1]:
            return -1
    if [card_val[i] for i in hand1] > [card_val[i] for i in hand2]:
        return 1
    else:
        return - 1
def solve1(lines):
    total = 0
    hands = [tuple(line.split()) for line in lines if line]
    list.sort(hands, key=functools.cmp_to_key(compare))
    print(hands)
    for i, (_, v) in enumerate(hands):
        total += (i + 1)*int(v)
    return total

def solve2(lines):
    total = 0
    return total


part1 = 0
part2 = 0
part1 += solve1(data)
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
# with open("test.txt", "r") as f:
#     data = f.readlines()
part2 += solve2(data)
print()
print(part1)
print(part2)
