import sys
from collections import deque

input = sys.stdin.readline

# 초기 문자열을 왼쪽 덱에 담음
left_deque = deque(input().strip())
right_deque = deque()

m = int(input())

for _ in range(m):
    command = input().split()
    
    if command[0] == 'L':
        if left_deque:
            # 왼쪽 끝에서 꺼내 오른쪽 앞에 추가
            right_deque.appendleft(left_deque.pop())
            
    elif command[0] == 'D':
        if right_deque:
            # 오른쪽 앞(커서 바로 옆)에서 꺼내 왼쪽 끝에 추가
            left_deque.append(right_deque.popleft())
            
    elif command[0] == 'B':
        if left_deque:
            left_deque.pop()
            
    elif command[0] == 'P':
        left_deque.append(command[1])

print("".join(left_deque) + "".join(right_deque))