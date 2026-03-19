n = int(input())
p = [0] + list(map(int, input().split()))
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = min(dp[i], p[k] + dp[i - k])

print(dp[n])