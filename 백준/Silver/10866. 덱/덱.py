import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        x = int(command[1])
        queue.appendleft(x)
    elif command[0] == 'push_back':
        x = int(command[1])
        queue.append(x)
    elif command[0] == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif command[0] == 'pop_back':
        print(queue.pop() if queue else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if not queue else 0)
    elif command[0] == 'front':
        print(queue[0] if queue else -1)
    elif command[0] == 'back':
        print(queue[-1] if queue else -1)