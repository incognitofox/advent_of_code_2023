import requests
from cookies import cookies
import re

day = 1
data = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies).text.split('\n')
print(data)

