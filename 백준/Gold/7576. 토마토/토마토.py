import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # n행 m열
    m, n = map(int, input().split())
    
    graph = []
    queue = deque()
    
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(m):
            # 익은 토마토(1)의 위치를 미리 큐에 삽입
            if row[j] == 1:
                queue.append((i, j))
                
    # 상, 하, 좌, 우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 창고 범위 내에 있고, 아직 익지 않은 토마토(0)인 경우
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    # 익은 날짜를 이전 값 + 1로 갱신
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    
    ans = 0
    for row in graph:
        for val in row:
            if val == 0:
                # 모두 익지 못하는 상황
                print(-1)
                return
            ans = max(ans, val)
    
    # 시작 값이 1이었으므로 최종 날짜에서 1을 뺌
    print(ans - 1)

solve()