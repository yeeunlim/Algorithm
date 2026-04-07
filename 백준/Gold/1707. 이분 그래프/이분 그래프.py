import sys
from collections import deque

input = sys.stdin.readline

def is_bipartite(v, adj):
    # visited 리스트: 0(미방문), 1(색상1), -1(색상2)
    visited = [0] * (v + 1)
    
    for i in range(1, v + 1):
        if visited[i] != 0:
            continue
            
        # BFS 시작
        queue = deque([i])
        visited[i] = 1  # 시작 노드 색상 지정
        
        while queue:
            curr = queue.popleft()
            
            for next_node in adj[curr]:
                if visited[next_node] == 0:
                    # 인접 노드를 현재 노드와 다른 색으로 칠함
                    visited[next_node] = -visited[curr]
                    queue.append(next_node)
                elif visited[next_node] == visited[curr]:
                    # 인접 노드의 색이 현재와 같다면 이분 그래프가 아님
                    return False
    return True

def solve():
    k = int(input())
    for _ in range(k):
        # 노드, 간선
        v, e = map(int, input().split())
        adj = [[] for _ in range(v + 1)]
        
        for _ in range(e):
            u, n = map(int, input().split())
            adj[u].append(n)
            adj[n].append(u)
        
        if is_bipartite(v, adj):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    solve()