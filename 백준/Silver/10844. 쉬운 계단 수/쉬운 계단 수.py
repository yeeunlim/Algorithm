n = int(input())
MOD = 1000000000
# dp[n][k]: 길이가 n이면서 마지막 숫자가 k인 경우의 수 
dp = [[0] * 10 for _ in range(n + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
        dp[i][j] %= MOD
        
print(sum(dp[n]) % MOD)