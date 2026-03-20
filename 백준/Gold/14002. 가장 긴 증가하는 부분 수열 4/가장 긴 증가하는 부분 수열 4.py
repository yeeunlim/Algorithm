import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))

    # dp[i]: i번째 원소를 마지막으로 하는 LIS의 길이
    dp = [1] * n
    # prev[i]: i번째 원소 이전의 원소 인덱스를 저장 (역추적용)
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            # 이전 원소보다 현재 원소가 더 크고
            if nums[j] < nums[i]:
                # 이전 수열에 덧붙이는게 더 길다면 업데이트, 이전 원소 인덱스 저장
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    # 최장 수열 길이
    max_len = max(dp)
    print(max_len)

    # 역추적을 통해 수열 구성하기
    curr_idx = dp.index(max_len)
    lis_path = []
    
    while curr_idx != -1:
        lis_path.append(nums[curr_idx])
        curr_idx = prev[curr_idx]

    # 역순으로 저장되었으므로 뒤집어서 출력
    print(*(lis_path[::-1]))

solve()