import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    # start부터 n까지 숫자 중 선택
    for i in range(start, n + 1):
        s.append(i)
        dfs(i) 
        s.pop()

dfs(1)