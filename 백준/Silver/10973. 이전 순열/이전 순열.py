def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # 뒤에서부터 오름차순이 끊기는 위치를 탐색
    # 2, 1, 3 -> 오름차순이 끊기는 2의 위치: i - 1
    i = n - 1
    while i > 0 and arr[i-1] < arr[i]:
        i -= 1
        
    if i == 0:
        print(-1)
        return

    # 2보다 작은 숫자를 찾아서 스왑
    # 2, 1, 3 -> 1, 2, 3
    j = n - 1
    while arr[i-1] < arr[j]:
        j -= 1
    
    arr[i-1], arr[j] = arr[j], arr[i-1]

    # 2 뒤의 숫자들을 내림차순으로 바꿈
    # 1, 2, 3 -> 1, 3, 2
    result = arr[:i] + arr[i:][::-1]
    print(*result)

solve()