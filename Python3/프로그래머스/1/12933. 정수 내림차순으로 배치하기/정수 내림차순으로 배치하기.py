def solution(n):
    # int -> str -> list -> str -> int
    return int("".join(sorted(str(n), reverse=True)))