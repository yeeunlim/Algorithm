import heapq
import sys

def solve():
    input = sys.stdin.readline
    
    # N: 보석 개수, K: 가방 개수
    n, k = map(int, input().split())
    
    # 보석 정보 (무게, 가격)
    jewels = []
    for _ in range(n):
        jewels.append(list(map(int, input().split())))
    
    # 가방 정보 (최대 수용 무게)
    bags = []
    for _ in range(k):
        bags.append(int(input()))
    
    # 무게 기준 오름차순 정렬
    jewels.sort()
    bags.sort()
    
    result = 0
    candidate_jewels = []
    jewel_idx = 0
    
    # 각 가방을 무게가 작은 순서대로 확인
    for bag_weight in bags:
        # 현재 가방에 담을 수 있는 무게의 보석들을 모두 후보군(힙)에 추가
        while jewel_idx < n and jewels[jewel_idx][0] <= bag_weight:
            # 최대 힙을 위해 가격에 -를 붙여 저장
            heapq.heappush(candidate_jewels, -jewels[jewel_idx][1])
            jewel_idx += 1
        
        # 후보군 중 가장 비싼 보석을 선택
        if candidate_jewels:
            # 마이너스를 다시 붙여 원래 가격으로 복구 후 합산
            result -= heapq.heappop(candidate_jewels)
            
    print(result)

if __name__ == "__main__":
    solve()