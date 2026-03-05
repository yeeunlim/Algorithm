import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())

visited = [False] * (n+1)

# 그래프 준비: 인접 리스트, 정렬
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# bfs
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)