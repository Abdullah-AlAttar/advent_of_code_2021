from collections import defaultdict
import sys
from termios import TIOCPKT_FLUSHWRITE
from typing import List
import math
import numpy as np

inputs = open(sys.argv[1], 'r').readlines()
usp = [
    pattern.split('|')[0].strip()
    for pattern in inputs
]
out_val = [
    pattern.split('|')[1].strip()
    for pattern in inputs
]

# print(usp)
counter = 0
for line, out in zip(usp, out_val):
    # print(line)
    # print(out)
    ps = {}
    ans = {}
    char_counts = defaultdict(int)
    for pattern in line.split():
        sz = len(pattern)
        if sz in ps:
            ps[sz].append(pattern)
        else :
            ps[sz] = [pattern]
        for char in pattern:
            char_counts[char] +=1
    # print('Counts', char_counts)
    for char, count in char_counts.items():
        if count == 4:
            bottom_left = char
        if count == 9:
            bottom_right = char
        if count == 6:
            top_left = char
    # print(ps)
    top = set(ps[3][0]) - set(ps[2][0])
    top = top.pop()
    bottom = set(ps[7][0]) - set(ps[4][0]) - set(f'{top}{bottom_left}')
    bottom = bottom.pop()
    for char, count in char_counts.items():
        if count == 7 and char !=bottom:
            middle = char
    top_right = set(ps[2][0]) - set(bottom_right)
    top_right = top_right.pop()
    # bottom = set(ps[7][0]) - set(f'{top}{top_left}{top_right}{bottom_left}{bottom_right}{middle}')
    # bottom = bottom.pop()
    
    # print(top, top_left, top_right, middle, bottom_left, bottom_right, bottom)
    
    ans[''.join(sorted(f'{top_right}{bottom_right}{top}{top_left}{bottom_left}{bottom}'))] = '0'
    ans[''.join(sorted(f'{top_right}{bottom_right}'))] = '1'
    ans[''.join(sorted(f'{top_right}{top}{middle}{bottom_left}{bottom}'))] = '2'
    ans[''.join(sorted(f'{top_right}{top}{middle}{bottom_right}{bottom}'))] = '3'
    ans[''.join(sorted(f'{top_right}{middle}{bottom_right}{top_left}'))] = '4'
    ans[''.join(sorted(f'{top}{middle}{bottom_right}{top_left}{bottom}'))] = '5'
    ans[''.join(sorted(f'{top}{middle}{bottom_right}{top_left}{bottom}{bottom_left}'))] = '6'
    ans[''.join(sorted(f'{top}{top_right}{bottom_right}'))] = '7'
    ans[''.join(sorted(f'{middle}{top_right}{bottom_right}{top}{top_left}{bottom_left}{bottom}'))] = '8'
    ans[''.join(sorted(f'{middle}{top_right}{bottom_right}{top}{top_left}{bottom}'))] = '9'
    res = []
    for pattern in out.split():
        print(pattern, ''.join(sorted(pattern)))
        print(ans[''.join(sorted(pattern))])
        res.append(ans[''.join(sorted(pattern))])
    print(''.join(res))
    counter += int(''.join(res))
            
print(counter)