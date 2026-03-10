from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    MAX = 100001
    dist = [0] * MAX
    queue = deque([start])
    dist[start] = 1
    
    while queue:
        x = queue.popleft()
        
        if x == end:
            return dist[x] - 1
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

print(bfs(n, k))