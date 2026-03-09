import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [-2, 2, 2, -2, 1, -1, 1, -1]
    
def bfs(x, y, a, b):
    queue = deque([(x, y)])
    dist = [[0] * i for _ in range(i)]
    dist[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if x == a and y == b:
            return dist[x][y] - 1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < i and 0 <= ny < i and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
                
for _ in range(n):
    i = int(input())
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    print(bfs(x, y, a, b))