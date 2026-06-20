def solution(land):
    # land: 석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열
    # 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return
    
    # dfs로 탐색하며 포함하는 열 set 구하기
    # 열별로 현재 덩어리의 area 더하기

    n, m = len(land), len(land[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(x, y):
        region_area = 0
        region_cols = set()

        stack = [(x, y)]
        visited[x][y] = True

        while stack:
            x, y = stack.pop()
            region_area += 1
            region_cols.add(y)

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if (0 <= nx < n and 0 <= ny < m
                    and not visited[nx][ny]
                    and land[nx][ny] == 1
                   ):
                    stack.append((nx, ny))
                    visited[nx][ny] = True

        return region_area, region_cols
                
    visited = [[False] * m for _ in range(n)]
    areas_per_col = [0] * m

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                region_area, region_cols = dfs(i, j)
                
                for col in region_cols:
                    areas_per_col[col] += region_area

    return max(areas_per_col)