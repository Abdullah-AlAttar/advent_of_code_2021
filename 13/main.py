import sys
import numpy as np
from PIL import Image

content = open(sys.argv[1]).readlines()
content, folds = content[:content.index('\n')], content[content.index('\n'):]

points = []
max_x = 0
max_y = 0

for line in content:
    points.append(tuple(map(lambda x: int(x), line.strip().split(','))))
    max_x = max(max_x, points[-1][0])
    max_y = max(max_y, points[-1][1])

grid = np.zeros((max_y + 1, max_x + 1), dtype=np.uint8)

for x, y in points:
    grid[y, x] = 1

print(grid.shape)


def fold_vertical(arr, n):
    up = arr[:n, :]
    down = np.flip(arr[n + 1:, :], axis=0)
    if up.shape[0] > down.shape[0]:
        down = np.pad(down, ((up.shape[0] - down.shape[0], 0), (0, 0)),
                      mode='constant',
                      constant_values=0)
    return up + down


def fold_hor(arr, n):
    # My input didn't need to handle differnt shapes case for horzinatol fold
    return np.flip(arr[:, n + 1:], axis=1) + arr[:, :n]


for fold in folds:
    print(fold)
    if not fold.strip():
        continue
    tmp = fold.split()[2]
    tmp = tmp.split('=')
    if tmp[0] == 'y':
        grid = fold_vertical(grid, int(tmp[1]))
    else:
        grid = fold_hor(grid, int(tmp[1]))
    print(np.count_nonzero(grid))

grid[np.where(grid >= 1)] = 255

img = Image.fromarray(grid)
img.save('wow.png')
