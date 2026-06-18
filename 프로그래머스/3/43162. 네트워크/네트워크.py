def solution(n, computers):
    visited = [False] * n
    
    def dfs(cur):
        visited[cur] = True
        # 다음 연결 노드 탐색
        for nxt in range(n):
            if computers[cur][nxt] == 1 and not visited[nxt]:
                dfs(nxt)
    
    answer = 0
    for node in range(n):
        if not visited[node]:
            dfs(node)
            answer += 1
    return answer