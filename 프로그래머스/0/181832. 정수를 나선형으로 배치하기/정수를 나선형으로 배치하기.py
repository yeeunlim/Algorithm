def solution(n):
    arr = [[0]*n for _ in range(n)]
    
    x, y = 0, 0
    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]
    direction = 0
    
    for val in range(1, n*n + 1):
        arr[x][y] = val
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 범위를 벗어나거나 이미 값이 있으면 방향 전환
        if not (0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0):
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x, y = nx, ny
    
    return arr
