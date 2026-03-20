import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    
    # DP 테이블 초기화
    dp = [0] * n
    dp[0] = nums[0]
    
    # 1부터 n-1까지 반복하며 최대 연속합 갱신
    for i in range(1, n):
        # (이전까지의 연속합 + 현재 숫자)와 (현재 숫자) 중 큰 것을 선택
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    
    # dp 리스트의 최댓값 출력
    print(max(dp))

if __name__ == "__main__":
    solve()