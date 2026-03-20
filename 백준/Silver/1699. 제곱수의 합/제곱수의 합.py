import sys

def solve():
    n = int(sys.stdin.readline())
    
    # dp[i]는 i를 만드는 제곱수 합의 최소 개수
    # 최악의 경우(1^2의 합)인 i로 초기화
    dp = [i for i in range(n + 1)]
    
    for i in range(1, n + 1):
        j = 1
        # i보다 작은 제곱수들을 모두 시도
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
            
    print(dp[n])

solve()