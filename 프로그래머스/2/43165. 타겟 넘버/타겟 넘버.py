def solution(numbers, target):   
    answer = 0
    def dfs(curr_idx, curr_sum):
        nonlocal answer
        # 종료: numbers 끝까지 탐색했을 때
        if curr_idx == len(numbers):
            # 목표 달성 시 answer + 1
            if curr_sum == target:
                answer += 1
            return
        
        # 현재 선택지: curr_index -> curr_sum에 curr_index의 값을 더하거나 뺀다
        dfs(curr_idx + 1, curr_sum + numbers[curr_idx])
        dfs(curr_idx + 1, curr_sum - numbers[curr_idx])
    dfs(0, 0)
    return answer