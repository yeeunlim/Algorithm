from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
que = deque()
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        que.append(int(command[1]))
    elif command[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        print(0 if que else 1)
    elif command[0] == 'front':
        print(que[0] if que else -1)
    elif command[0] == 'back':
        print(que[-1] if que else -1)