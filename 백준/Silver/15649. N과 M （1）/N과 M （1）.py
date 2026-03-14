import sys

n, m = map(int, sys.stdin.readline().split())

s = []  # 수열을 담을 스택
visited = [False] * (n + 1)  # 숫자 사용 여부 확인

def dfs():
    # 수열의 길이가 m에 도달하면 출력 후 종료
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if not visited[i]:  # 아직 사용하지 않은 숫자인 경우
            visited[i] = True
            s.append(i)
            dfs()           # 다음 숫자 선택을 위한 재귀 호출
            s.pop()         # 탐색 후 스택에서 제거 (Backtrack)
            visited[i] = False

dfs()