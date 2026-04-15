n = int(input())
path = []
visited = [False] * (n + 1)

def dfs():
    # 수열 완성 시 출력
    if len(path) == n:
        print(*path)
        return
    
    # dfs 탐색
    for i in range(1, n + 1):
        if not visited[i]:
            path.append(i)
            visited[i] = True

            dfs()

            # 백트래킹
            path.pop()
            visited[i] = False

dfs()