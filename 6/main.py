from collections import defaultdict
import sys
from typing import List

a = list(map(int, open(sys.argv[1], 'r').read().split(',')))
print(a)


def get_fishes(a: List[int], ndays: int):
    for _ in range(ndays):
        new_fishes = []
        for i in range(len(a)):
            if a[i] == 0:
                new_fishes.append(8)
                a[i] = 6
            else:
                a[i] -= 1
        a += new_fishes
        # print(a)


def get_fishes_fast(a: List[int], ndays: int):
    counts = defaultdict(int)
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    print(counts)
    for _ in range(ndays):
        sums = defaultdict(int)
        for k, v in counts.items():
            if k == 0:
                sums[6] += v
                sums[8] += v
            else:
                sums[k - 1] += v
        counts = sums
    print(counts)
    return sum(counts.values())


print(get_fishes_fast(a, 256))
# print(len(a))
