import sys

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    # LCM = (A * B) // GCD
    print((a * b) // get_gcd(a, b))