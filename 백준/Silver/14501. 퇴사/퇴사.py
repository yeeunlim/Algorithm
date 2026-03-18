import sys

def solve():
    input = sys.stdin.readline
    N = int(input())

    T = [0] * N
    P = [0] * N

    # 데이터 입력 받기
    for i in range(N):
        T[i], P[i] = map(int, input().split())

    # DP 테이블 (퇴사일 이후의 값을 처리하기 위해 N+1 크기로 안전하게 할당)
    dp = [0] * (N + 1)

    # 마지막 날부터 0번째 날까지 거꾸로 역순 계산
    for i in range(N - 1, -1, -1):
        # 상담을 완료하는 데 걸리는 기간이 퇴사일을 넘어가는 경우
        if i + T[i] > N:
            dp[i] = dp[i + 1]
        # 상담을 기한 내에 마칠 수 있는 경우
        else:
            dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

    # 0번째 날(첫 날)부터 시작했을 때의 최대 수익 출력
    print(dp[0])

if __name__ == '__main__':
    solve()