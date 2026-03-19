import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

s = []

def dfs(depth):
    if depth == m:
        print(*s)
        return

    for i in range(n):
        s.append(arr[i])
        dfs(depth + 1)
        s.pop()

dfs(0)