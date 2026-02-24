def solution(prices):
    n = len(prices)
    answer = [0] * n
    # 아직 가격이 떨어지지 않은 시점의 '인덱스'를 담을 스택
    waiting_stack = []
    
    for current_time, current_price in enumerate(prices):
        # 1. 가격이 떨어진 경우 처리
        # 스택이 비어있지 않고, 현재 가격이 스택 맨 위의 가격보다 낮다면
        while waiting_stack and prices[waiting_stack[-1]] > current_price:
            past_time = waiting_stack.pop()
            # 현재 시간과 과거 시간의 차이가 유지 시간
            answer[past_time] = current_time - past_time
        
        # 2. 현재 시점의 인덱스를 스택에 추가
        waiting_stack.append(current_time)
    
    # 3. 끝까지 가격이 떨어지지 않은 시점들 처리
    while waiting_stack:
        past_time = waiting_stack.pop()
        # 전체 길이(마지막 인덱스)에서 해당 시점의 인덱스를 뺌
        answer[past_time] = (n - 1) - past_time
        
    return answer