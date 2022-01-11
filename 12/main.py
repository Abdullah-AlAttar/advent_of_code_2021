from collections import defaultdict
import sys

edges = open(sys.argv[1]).readlines()

graph = defaultdict(list)
for edge in edges:
    start, end = edge.strip().split('-')
    
    graph[start].append(end)
    if start !='start':
        graph[end].append(start)
print(graph)
counter = 0

def dfs(graph, node, visited):
    print(node)
    global counter
    if node == 'end':
        counter += 1
        return
    if not node.isupper():
        visited.add(node)

    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)


visited = set()
dfs(graph, 'start', visited)
print(visited)
print(counter)
