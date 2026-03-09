from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0)])
    dist[0][0] = 1  # 시작 칸도 포함
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist[n-1][m-1]

print(bfs())