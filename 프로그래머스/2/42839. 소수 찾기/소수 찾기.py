from itertools import permutations

def check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    p_set = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            p_set.add(int("".join(p)))
    return len(list(filter(check, p_set)))