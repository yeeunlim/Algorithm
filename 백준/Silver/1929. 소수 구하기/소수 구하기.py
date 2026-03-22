import sys

def find_primes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    # 에라토스테네스의 체
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i가 소수라면, i의 배수들은 소수가 아니므로 False로 처리
            # i*k (k < i)인 배수들은 이미 이전 소수에 의해 처리되었으므로 i*i부터 시작
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    # m 이상 n 이하의 숫자 중 소수(True)인 것만 출력
    for i in range(m, n + 1):
        if is_prime[i]:
            print(i)

m, n = map(int, sys.stdin.readline().split())
find_primes(m, n)