import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y, m, n, field):
    # 상하좌우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 현재 위치 방문 처리 (배추를 0으로 바꿈)
    field[y][x] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 밭 범위 내에 있고, 배추(1)가 심어져 있는 경우 재귀 탐색
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] == 1:
                dfs(nx, ny, m, n, field)

def solve():
    t = int(input())  # 테스트 케이스 개수
    
    for _ in range(t):
        m, n, k = map(int, input().split())  # 가로, 세로, 배추 개수
        field = [[0] * m for _ in range(n)]
        count = 0
        
        # 배추 위치 입력
        for _ in range(k):
            x, y = map(int, input().split())
            field[y][x] = 1
            
        # 밭 전체를 순회
        for i in range(n):
            for j in range(m):
                if field[i][j] == 1:  # 배추가 있는 곳에서 탐색 시작
                    dfs(j, i, m, n, field)
                    count += 1
        
        print(count)

if __name__ == "__main__":
    solve()