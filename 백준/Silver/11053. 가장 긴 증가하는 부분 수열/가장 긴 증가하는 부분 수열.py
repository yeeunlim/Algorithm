import sys

def solve():
    # 입력 받기
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp 배열을 1로 초기화 (최소 길이는 자기 자신인 1)
    dp = [1] * n
    
    # 이중 반복문을 통한 DP 수행
    for i in range(n):
        for j in range(i):
            # 현재 숫자(a[i])가 이전 숫자(a[j])보다 크다면
            if a[j] < a[i]:
                # j번째까지의 LIS 길이에 현재 숫자를 추가한 것(+1)과 
                # 현재 dp[i] 값 중 최댓값으로 갱신
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 전체 dp 배열 중 가장 큰 값이 수열의 LIS 길이임
    print(max(dp))

solve()