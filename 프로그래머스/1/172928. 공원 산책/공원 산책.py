def solution(park, routes):
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    # 초기 위치
    h, w = len(park), len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                r, c = i, j
                break
    for route in routes:
        op, n = route.split()
        n = int(n)
        dr, dc = direction[op]
        nr, nc = r, c
        for _ in range(n):
            nr += dr
            nc += dc
            if nr < 0 or nr >= h or nc < 0 or nc >= w or park[nr][nc] == 'X':
                break
        else:
            r, c = nr, nc
    return [r, c]