import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    # 뒤에서부터 인접한 두 원소를 비교해 내림차순이 끊기는 지점(i-1) 찾기
    i = n - 1  # 마지막 인덱스
    while i > 0 and a[i-1] > a[i]:
        i -= 1
    
    # 마지막 순열인 경우
    if i == 0:
        print(-1)
        return

    # 다시 뒤에서부터 a[i-1]보다 큰 첫 번째 원소(j) 찾기
    j = n - 1 # 마지막 인덱스
    while a[i-1] > a[j]:
        j -= 1

    # i-1과 j를 스왑
    a[i-1], a[j] = a[j], a[i-1]
    
    # i번째 인덱스부터 끝까지 뒤집기 (이미 내림차순이므로 뒤집으면 오름차순이 됨)
    result = a[:i] + a[i:][::-1]

    print(*result)

solve()