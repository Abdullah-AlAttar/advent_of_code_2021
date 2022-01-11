from collections import defaultdict
import sys
from typing import List
import math
import numpy as np

a = list(map(int, open(sys.argv[1], 'r').read().split(',')))
def naive():
    sums = []
    for i in range(min(a), max(a)):
        res = 0
        for e in a:
            dif = abs(e - i)
            res += (dif * (dif + 1)) / 2
        sums.append(res)
    return min(sums)
print(a)
print(naive())
