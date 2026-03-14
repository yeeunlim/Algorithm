import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # 1부터가 아니라 start부터 시작함으로써 이전 숫자보다 큰 것만 선택함
    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)  # 현재 숫자 i보다 1 큰 숫자부터 뽑도록 전달
            s.pop()

dfs(1)