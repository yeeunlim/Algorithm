from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0, 1)])
    visited[0][0] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < n and 0 <= ny < m
                and not visited[nx][ny]
                and maps[nx][ny] == 1
            ):
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1