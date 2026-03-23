import sys

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    # n = a + b 에서 a는 가장 작은 홀수 소수인 3부터 시작
    # b-a가 가장 큰 것을 출력해야 하므로, a가 가장 작을 때 바로 종료
    for a in range(3, n // 2 + 1, 2):
        if is_prime[a] and is_prime[n - a]:
            print(f"{n} = {a} + {n - a}")
            break
    else:
        print("Goldbach's conjecture is wrong.")