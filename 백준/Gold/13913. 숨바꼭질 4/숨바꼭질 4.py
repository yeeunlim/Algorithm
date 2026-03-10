from collections import deque
import sys

input = sys.stdin.readline
MAX = 100001

def bfs(start, end):
    """최단 거리와 부모 노드 정보를 계산하여 반환"""
    dist = [-1] * MAX
    parent = [-1] * MAX
    
    queue = deque([start])
    dist[start] = 0
    
    while queue:
        curr = queue.popleft()
        
        if curr == end:
            return dist, parent
            
        for nx in (curr - 1, curr + 1, curr * 2):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[curr] + 1
                parent[nx] = curr
                queue.append(nx)
    return dist, parent

def get_path(start, end, parent):
    """parent 배열을 역추적하여 경로 리스트 생성"""
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]

def solve():
    n, k = map(int, input().split())
    
    dist, parent = bfs(n, k)

    print(dist[k])
    path = get_path(n, k, parent)
    print(*path)

solve()