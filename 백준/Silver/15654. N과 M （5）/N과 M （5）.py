n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
visited = [False] * n

def dfs(depth):
    if depth == m:
        print(*s)
        return
    for i in range(n):
        if not visited[i]:
            s.append(arr[i])
            visited[i] = True
            dfs(depth + 1)
            s.pop()
            visited[i] = False
            
dfs(0)