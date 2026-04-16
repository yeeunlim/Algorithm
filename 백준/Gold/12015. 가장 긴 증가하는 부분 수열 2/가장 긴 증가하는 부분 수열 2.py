import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.read().split()
    n = int(input[0])
    v = list(map(int, input[1:]))
    
    lis = [v[0]]
    
    for i in range(1, n):
        # 현재 값이 LIS의 마지막 값보다 크면 뒤에 추가
        if v[i] > lis[-1]:
            lis.append(v[i])
        else:
            # 그렇지 않으면 이분 탐색으로 대치할 위치를 찾음
            idx = bisect_left(lis, v[i])
            lis[idx] = v[i]
            
    print(len(lis))

if __name__ == "__main__":
    solve()