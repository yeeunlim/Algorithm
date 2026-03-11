import sys

heights = [int(sys.stdin.readline()) for _ in range(9)]
heights.sort()

total_sum = sum(heights)
target = total_sum - 100

def solve():
    for i in range(9):
        for j in range(i + 1, 9):
            # 두 명의 합이 target과 같다면 그 둘을 제외하고 출력
            if heights[i] + heights[j] == target:
                for k in range(9):
                    if k != i and k != j:
                        print(heights[k])
                return

solve()