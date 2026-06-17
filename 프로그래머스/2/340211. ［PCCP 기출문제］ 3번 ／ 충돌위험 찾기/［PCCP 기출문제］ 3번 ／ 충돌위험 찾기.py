from collections import defaultdict

def solution(points, routes):
    answer = 0
    
    # {시간: {좌표: 로봇 수}}
    # time_positions[t][(r, c)] = 해당 시간 t에 그 좌표에 있는 로봇 수
    time_positions = defaultdict(lambda: defaultdict(int))
    
    # 로봇별 운송경로
    # [[2, 3, 4, 5], [1, 3, 4, 5]]
    for route in routes:
        time = 0

        # 시작 위치
        r, c = points[route[0] - 1]
        time_positions[time][(r, c)] += 1

        # 경유지들을 순서대로 이동
        # [2, 3, 4, 5]
        for i in range(1, len(route)):
            nr, nc = points[route[i] - 1]

            # r 좌표 먼저 이동
            while r != nr:
                time += 1
                if r < nr:
                    r += 1
                else:
                    r -= 1
                time_positions[time][(r, c)] += 1

            # c 좌표 이동
            while c != nc:
                time += 1
                if c < nc:
                    c += 1
                else:
                    c -= 1
                time_positions[time][(r, c)] += 1

    # 같은 시간, 같은 좌표에 2대 이상 있으면 충돌 위험 1회
    for positions in time_positions.values():
        for count in positions.values():
            if count >= 2:
                answer += 1

    return answer