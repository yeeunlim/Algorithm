import sys

def check_max_candy(n, board):
    max_cnt = 1
    for i in range(n):
        # 가로 확인
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt) # 루프가 끝난 후 마지막 연속 구간 갱신

        # 세로 확인
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt) # 루프가 끝난 후 마지막 연속 구간 갱신
        
    return max_cnt

def solve():
    input = sys.stdin.readline
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except (EOFError, ValueError):
        return

    board = [list(input().strip()) for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            # 오른쪽 사탕과 교환
            if j + 1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                ans = max(ans, check_max_candy(n, board))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # 아래쪽 사탕과 교환
            if i + 1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                ans = max(ans, check_max_candy(n, board))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                
    print(ans)

if __name__ == "__main__":
    solve()