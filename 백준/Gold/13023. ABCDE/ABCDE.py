import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n

    def dfs(node, depth):
        if depth == 4:
            print(1)
            sys.exit()
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                dfs(nxt, depth + 1)
        visited[node] = False   # 백트래킹

    for i in range(n):
        dfs(i, 0)

    print(0)

solve()