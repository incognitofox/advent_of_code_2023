import requests
from cookies import cookies
import re
import math

day = 4
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
nums = {"one": 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine": 9, "zero":0}

red_start = 12
green_start = 13
blue_start = 14

# with open("test.txt", "r") as f:
#     data = f.readlines()

starts = {"red": 12, "green": 13, "blue": 14}

def solve1(lines):
    total = 0
    for line in lines:
        if line:
            parts = line.split(":")
            hands = parts[1].strip().split("|")
            left = hands[0].strip().split()
            right = hands[1].strip().split()
            count = 0
            for val in right:
                if val in left:
                    total += math.pow(2, max(0, count - 1))
                    count += 1
    return total


def solve2(lines):
    total = 0
    cards = {}
    copies = {}
    frontier = []
    for line in lines:
        if line:
            parts = line.split(":")
            card_id = parts[0].strip().split()[1]
            hands = parts[1].strip().split("|")
            left = hands[0].strip().split()
            right = hands[1].strip().split()
            count = 0
            for val in right:
                if val in left:
                    count += 1
            cards[card_id] = count
            copies[card_id] = 1
            frontier.append(card_id)
    total = sum(copies.values())
    while sum(copies.values()) > 0:
        new_copies = {c: 0 for c in copies}
        for card in copies:
            if copies[card] > 0:
                for i in range(cards[card]):
                    new_copies[str(int(card)+ i + 1)] += copies[card]
                total += copies[card]*cards[card]
        copies = new_copies.copy()
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
