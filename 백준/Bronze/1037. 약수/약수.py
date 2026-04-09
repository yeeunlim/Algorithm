import sys

count = int(sys.stdin.readline())

divisors = list(map(int, sys.stdin.readline().split()))

result = min(divisors) * max(divisors)

print(result)