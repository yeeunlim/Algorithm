import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    stack = []
    line = input().strip()
    
    is_vps = True
    for char in line:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if is_vps and not stack:
        print('YES')
    else:
        print('NO')