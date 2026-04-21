import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
 
    matrix_a = [list(map(int, list(input().strip()))) for _ in range(n)]
    matrix_b = [list(map(int, list(input().strip()))) for _ in range(n)]

    def flip(r, c):
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                # 0은 1로, 1은 0으로 반전
                matrix_a[i][j] = 1 - matrix_a[i][j]

    flip_count = 0

    # 행렬을 순회하며 값이 다를 경우 뒤집기 수행
    for i in range(n - 2):
        for j in range(m - 2):
            if matrix_a[i][j] != matrix_b[i][j]:
                flip(i, j)
                flip_count += 1

    if matrix_a == matrix_b:
        print(flip_count)
    else:
        print(-1)

if __name__ == "__main__":
    solve()