import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
ans = 64
for i in range(n - 7):
    for j in range(m - 7):
        draw_w = 0
        draw_b = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] == 'W':
                        draw_b += 1
                    elif board[a][b] == 'B':
                        draw_w += 1
                elif (a + b) % 2 == 1:
                    if board[a][b] == 'W':
                        draw_w += 1
                    elif board[a][b] == 'B':
                        draw_b += 1
        ans = min(ans, draw_w, draw_b)
        
print(ans)