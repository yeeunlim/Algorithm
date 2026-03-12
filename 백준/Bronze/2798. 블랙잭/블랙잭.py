n, m = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            current_sum = numbers[i] + numbers[j] + numbers[k]
            if current_sum <= m:
                ans = max(ans, current_sum)
print(ans)