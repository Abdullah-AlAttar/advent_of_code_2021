import sys
import numpy as np

grid = np.array([[int(char) for char in line.strip()]
                 for line in open(sys.argv[1]).readlines()])

grid = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

visited = np.zeros(grid.shape)
counter = 0

def flash(step : int):
    global counter
    global visited
    while True:
        flashed = False
        for r in range(1, grid.shape[0] - 1):
            for c in range(1, grid.shape[1] - 1):
                if grid[r, c] > 9 and visited[r, c] == 0:
                    flashed = True
                    counter += 1
                    visited[r, c] = 1
                    # grid[r,c] -= 9
                    grid[r - 1, c - 1] += 1
                    grid[r + 1, c - 1] += 1
                    grid[r - 1, c] += 1
                    grid[r + 1, c] += 1
                    grid[r, c - 1] += 1
                    grid[r, c + 1] += 1
                    grid[r + 1, c + 1] += 1
                    grid[r - 1, c + 1] += 1
        if not flashed:
            break
    grid[np.where(visited == 1)] = 0
    
    if np.all(grid[1:-1, 1:-1] == 0):
        print('Yes', step + 1) 
        exit()
    visited = np.zeros(grid.shape)
    


for i in range(2000):
    grid += 1
    flash(i)