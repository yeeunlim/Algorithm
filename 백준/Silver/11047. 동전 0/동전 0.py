import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

cnt = 0
for coin in coins:
    if k == 0: # 남은 금액이 없으면 종료
        break
    
    # 현재 동전으로 채울 수 있는 개수를 한 번에 더함
    cnt += k // coin
    # 남은 금액을 나머지 연산으로 갱신
    k %= coin

print(cnt)