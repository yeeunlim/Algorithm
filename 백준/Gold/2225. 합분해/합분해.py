import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())
MOD = 1000000000

# dp[k][n]: 정수 k개를 사용하여 합이 n이 되는 경우의 수
dp = [[0] * (n + 1) for _ in range(k + 1)]

# 초기값 설정
for i in range(1, k + 1):
    dp[i][0] = 1
for i in range(1, n + 1):
    dp[1][i] = 1

# 점화식에 따라 DP 테이블 채우기
for i in range(2, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

# 결과 출력
print(dp[k][n])