from collections import deque

def is_valid(place):
    n = 5
    # P 사이 거리 2 이하, 파티션 없으면 거리두기 x -> False
    def bfs(sx, sy):
        q = deque()
        visited = [[False] * n for _ in range(n)]
        q.append((sx, sy, 0))
        visited[sx][sy] = True
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        while q:
            x, y, dist = q.popleft()
            if dist >= 2:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 범위 안에 있고, 방문하지 않았으면
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if place[nx][ny] == 'O':
                        q.append((nx, ny, dist + 1))
                        visited[nx][ny] = True
                    elif place[nx][ny] == 'P':
                        return False
        return True
                    
    
    # P 찾기(bfs 시작점)
    for i in range(n):
        for j in range(n):
            if place[i][j] == 'P':
                if not bfs(i, j):
                    return 0
    return 1
                        
def solution(places):
    return [is_valid(place) for place in places]
        
        