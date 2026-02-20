import sys
T = int(sys.stdin.readline())
for _ in range(T):
    words = sys.stdin.readline().split()
    print(" ".join([word[::-1] for word in words]))