n = int(input())

def draw_stars(n):
    # 기본 단위인 n=1일 때 별 하나를 리스트에 담아 반환
    if n == 1:
        return ['*']

    # n/3 크기의 별 패턴을 재귀적으로 가져옴
    stars = draw_stars(n // 3)
    result = []

    # 상단: 이전 패턴을 3번 가로로 이어붙임
    for s in stars:
        result.append(s * 3)
    
    # 중단: 이전 패턴 + 공백(n/3 크기) + 이전 패턴
    for s in stars:
        result.append(s + ' ' * (n // 3) + s)
    
    # 하단: 상단과 동일하게 3번 이어붙임
    for s in stars:
        result.append(s * 3)
    return result

print('\n'.join(draw_stars(n)))