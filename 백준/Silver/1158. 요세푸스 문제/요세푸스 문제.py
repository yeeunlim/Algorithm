from collections import deque
n, k = map(int, input().split())
que = deque(str(i) for i in range(1, n+1))
answer = []
while que:
    for i in range(1, k+1):
        if i == k:
            answer.append(que.popleft())
        else:
            que.append(que.popleft())
print("<" + ", ".join(answer) + ">")