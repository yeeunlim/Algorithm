import sys

input = sys.stdin.readline

n = int(input())
# 1. 정수(int)로 변환하여 리스트 생성
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_diff = float('inf')

def backtrack(depth, start_idx):
    global min_diff
    
    if depth == n // 2:
        start_team_score = 0
        link_team_score = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    # 이제 정수 연산이 정상적으로 이루어집니다.
                    start_team_score += board[i][j] + board[j][i]
                elif not visited[i] and not visited[j]:
                    link_team_score += board[i][j] + board[j][i]
        
        diff = abs(start_team_score - link_team_score)
        if diff < min_diff:
            min_diff = diff
        return

    for i in range(start_idx, n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth + 1, i + 1)
            visited[i] = False
            
            # 조기 종료 최적화
            if min_diff == 0:
                return

backtrack(0, 0)
print(min_diff)