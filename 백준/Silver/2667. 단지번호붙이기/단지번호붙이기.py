import sys

sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline
    n = int(input())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        visited[x][y] = True
        count = 1  # 현재 집 카운트
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    # 다음 집으로 더 깊이 탐색하며 반환된 카운트를 합산
                    count += dfs(nx, ny)
        return count

    complex_counts = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                complex_counts.append(dfs(i, j))

    print(len(complex_counts))
    for count in sorted(complex_counts):
        print(count)

solve()