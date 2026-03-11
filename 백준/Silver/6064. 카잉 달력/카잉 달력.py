import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    
    result = -1
    # x부터 시작해서 m씩 증가하며 탐색
    for k in range(x, m * n + 1, m):
        if (k - y) % n == 0:
            result = k
            break
    
    print(result)