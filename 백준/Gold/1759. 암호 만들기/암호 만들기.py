import sys

input = sys.stdin.readline

def solve():
    l, c = map(int, input().split())
    arr = sorted(input().split())
    
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    s = []

    def dfs(start, v_cnt, c_cnt):
        if len(s) == l:
            if v_cnt >= 1 and c_cnt >= 2:
                print(''.join(s))
            return
        
        for i in range(start, c):
            char = arr[i]
            s.append(char)
            
            # 재귀 호출 시 현재 문자가 모음인지 자음인지 판별하여 개수 갱신
            if char in vowels_set:
                dfs(i + 1, v_cnt + 1, c_cnt)
            else:
                dfs(i + 1, v_cnt, c_cnt + 1)
            
            s.pop()

    dfs(0, 0, 0)

solve()