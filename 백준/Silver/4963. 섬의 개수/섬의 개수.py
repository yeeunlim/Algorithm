import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1,  0,  1,-1, 1,-1, 0, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count)