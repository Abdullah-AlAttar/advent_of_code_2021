from dataclasses import dataclass
import sys
from typing import List
import numpy as np


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    a: Point
    b: Point


with open(sys.argv[1], 'r') as f:
    points: List[Line] = []

    min_x = 999999999999
    min_y = 999999999999
    max_x = -1
    max_y = -1

    for line in f:
        x1, y1, x2, y2 = map(int, line.replace('->', ',').split(','))
        min_x = min(min_x, x1, x2)
        min_y = min(min_y, y1, y2)
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
        points.append(Line(Point(x1, y1), Point(x2, y2)))

    mask = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for line in points:
        line.a.x -= min_x
        line.b.x -= min_x
        line.a.y -= min_y
        line.b.y -= min_y
    print(mask)
    print(points)
    print(min_x, min_y, max_x, max_y)
    for line in points:
        print(line)
        if line.a.y == line.b.y:
            mask[line.a.y,
                 min(line.a.x, line.b.x):max(line.a.x, line.b.x) + 1] += 1
        if line.a.x == line.b.x:
            mask[min(line.a.y, line.b.y):max(line.a.y, line.b.y) + 1,
                 line.a.x] += 1
        if line.a.x == line.a.y and line.b.x == line.b.y:
            print('yes')
            for i in range(min(line.a.x, line.b.x),
                           max(line.a.x, line.b.x) + 1):
                mask[i, i] += 1
        if sorted([line.a.x, line.a.y]) == sorted([line.b.x, line.b.y]):
            
            print("Yes", line, 1 if line.a.x < line.b.y else -1)
            print( list(range(line.a.x, line.b.x,
                           1 if line.a.x < line.b.y else -1)) )
            for i, j in zip(
                    range(line.a.x, line.b.x + 1 if line.a.x < line.b.y else -1,
                          1 if line.a.x < line.b.y else -1),
                    range(line.a.y, line.b.y + 1 if line.a.y < line.b.y else -1,
                          1 if line.a.y < line.b.y else -1)):
                print(i, j)
                mask[i, j] += 1
        print(mask)
    print(mask[mask >= 2], len((mask[mask >= 2])))
