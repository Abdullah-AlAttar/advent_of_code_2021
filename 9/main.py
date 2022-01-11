import sys
import numpy as np

grid = np.array([[int(char) for char in line.strip()]
                 for line in open(sys.argv[1]).readlines()])

grid = np.pad(grid,
              pad_width=1,
              mode='constant',
              constant_values=np.amax(grid) )
# ans = 0 
# for x in range(1, grid.shape[0] - 1):
#     for y in range(1, grid.shape[1] - 1):
#         p = grid[x, y]
#         top = grid[x - 1, y]
#         bottom = grid[x + 1, y]
#         right = grid[x, y + 1]
#         left = grid[x, y - 1]
#         if p < top and p < bottom and p < right and p < left:
#             print("nice", p)
#             ans += p + 1

# print(ans)
visited = np.zeros(grid.shape)
visited[np.where(grid==9)] = 1
print(visited)

def visit(a : int, b :int):
    queue = []
    queue.append((a, b))
    visited[a, b] = 1
    counter = 0
    while queue:
        x, y = queue.pop(0)
        counter +=1
        if visited[x - 1, y] == 0:
            queue.append((x-1, y))
            visited[x-1, y] = 1
            
        if visited[x +1, y] == 0:
            queue.append((x+1, y))
            visited[x+1, y] = 1
            
        if visited[x, y-1] == 0:
            queue.append((x, y-1))
            visited[x, y-1] = 1
            
        if visited[x, y + 1] == 0:
            queue.append((x, y+1))
            visited[x, y+1] = 1       
    return counter
anss =[]
for x in range(1, grid.shape[0] - 1):
    for y in range(1, grid.shape[1] - 1):
        if visited[x,y] == 0:
            anss.append(visit(x,y))
ans = sorted(anss)[-3:]
print(ans[0] * ans[2] * ans[1])
            