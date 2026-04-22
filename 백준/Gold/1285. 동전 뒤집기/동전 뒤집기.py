import sys

def solve():
    input = sys.stdin.read().split()
    
    n = int(input[0])
    board = []
    for i in range(n):
        row_str = input[i+1]
        row_val = 0
        for j in range(n):
            if row_str[j] == 'T':
                row_val |= (1 << j)
        board.append(row_val)

    ans = n * n

    for bit in range(1 << n):
        total_tails = 0
        
        for j in range(n):
            tails_count = 0
            for i in range(n):
                current_state = (board[i] >> j) & 1
                
                # 행이 뒤집히는 경우 (bit의 i번째 비트가 1인 경우)
                if (bit >> i) & 1:
                    current_state = 1 - current_state
                
                if current_state == 1:
                    tails_count += 1
            
            total_tails += min(tails_count, n - tails_count)
        
        # 최솟값 업데이트
        if total_tails < ans:
            ans = total_tails
            
    print(ans)

if __name__ == "__main__":
    solve()