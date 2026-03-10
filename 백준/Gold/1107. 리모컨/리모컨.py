import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    
    # 고장난 버튼 집합 생성
    broken_buttons = set()
    if m > 0:
        broken_buttons = set(input().split())

    # 최솟값 초기화: 현재 채널(100)에서 '+' 또는 '-' 버튼만 눌러 이동하는 경우
    min_press = abs(n - 100)
    
    # 0부터 1,000,000번 채널까지 모든 경우의 수 탐색(500000보다 높은 숫자에서 내려오는 경우를 포함)
    for channel in range(1000001):
        channel_str = str(channel)
        
        # 누를 수 없는 채널이면 break
        for digit in channel_str:
            if digit in broken_buttons:
                break
        else:
            # 총 누르는 횟수 = (채널 숫자의 길이) + (해당 채널에서 목표 채널까지 +, -를 누르는 횟수)
            press = len(channel_str) + abs(n - channel)
            min_press = min(min_press, press)
            
    print(min_press)

if __name__ == "__main__":
    solve()