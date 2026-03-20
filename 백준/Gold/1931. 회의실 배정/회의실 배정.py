import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    
    # 정렬 기준 설정
    # 1순위: 종료 시간 (x[1]) 오름차순
    # 2순위: 시작 시간 (x[0]) 오름차순
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    count = 0
    last_end_time = 0
    
    # 정렬된 회의를 순차적으로 확인
    for start, end in meetings:
        # 현재 회의의 시작 시간이 이전 회의의 종료 시간보다 크거나 같으면 선택
        if start >= last_end_time:
            count += 1
            last_end_time = end  # 다음 회의 선택을 위해 종료 시간 갱신
            
    print(count)

if __name__ == "__main__":
    solve()