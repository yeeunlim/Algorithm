import sys
from collections import deque

T = int(sys.stdin.readline())
stack = deque()

for i in range(T):
    a = sys.stdin.readline().split()
    for j in a:
        stack.extend(j)
        while stack:
            print(stack.pop(), end='')
        print(end=' ')