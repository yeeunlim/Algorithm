def solution(n, m, section):
    last_painted = 0
    count = 0
    for s in section:
        if s > last_painted:
            last_painted = s + m - 1
            count += 1
    return count