import sys

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_sum = 0
    max_val = max(map(max, grid))
    
    def dfs(x, y, depth, current_sum):
        nonlocal max_sum
        # 현재 합 + 남은 칸 * 최댓값이 max_sum보다 작으면 중단
        if current_sum + max_val * (4 - depth) <= max_sum:
            return
        
        if depth == 4:
            max_sum = max(max_sum, current_sum)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, current_sum + grid[nx][ny])
                visited[nx][ny] = False # 백트래킹 복구

    def check_t_shape(x, y):
        nonlocal max_sum
        center_val = grid[x][y]
        wings = []
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                wings.append(grid[nx][ny])
        
        # 날개가 4개면 가장 작은 것 하나를 버림
        if len(wings) == 4:
            max_sum = max(max_sum, center_val + sum(wings) - min(wings))
        # 날개가 딱 3개면 그 자체로 'ㅗ' 계열 모양 완성
        elif len(wings) == 3:
            max_sum = max(max_sum, center_val + sum(wings))
    
    for i in range(N):
        for j in range(M):
            visited[i][j] = True # 시작점 방문 처리
            dfs(i, j, 1, grid[i][j])
            visited[i][j] = False # 시작점 방문 해제
            check_t_shape(i, j)
            
    print(max_sum)

if __name__ == '__main__':
    solve()