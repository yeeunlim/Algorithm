import sys

def solve():
    input = sys.stdin.readline
 
    T = int(input().strip())
    
    MAX_N = 100000
    MOD = 1000000009
    
    # dp[n][1], dp[n][2], dp[n][3]
    dp = [[0] * 4 for _ in range(MAX_N + 1)]
    
    # 초기값 설정
    dp[1][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1 # 2+1
    dp[3][2] = 1 # 1+2
    dp[3][3] = 1 # 3
    
    # 점화식 수행
    for i in range(4, MAX_N + 1):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD
    
    results = []
    for _ in range(T):
        n_str = input().strip()
        n = int(n_str)
        ans = (dp[n][1] + dp[n][2] + dp[n][3]) % MOD
        results.append(str(ans))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()