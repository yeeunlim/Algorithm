def solution(s):
    answer = 0
    count_target = 0    # 기준 문자의 등장 횟수
    count_others = 0    # 기준 문자가 아닌 다른 문자의 등장 횟수
    target_char = ""    # 현재 그룹의 기준 문자

    for char in s:
        # 두 카운트가 같으면 새로운 그룹이 시작되는 시점
        if count_target == count_others:
            answer += 1
            target_char = char  # 현재 문자를 새로운 기준 문자로 설정
        
        # 현재 문자가 기준 문자인지 여부에 따라 카운트를 올림
        if char == target_char:
            count_target += 1
        else:
            count_others += 1
            
    return answer

# 루프 끝에서 카운트 올린 후 검사 시: 마지막에는 count 같아도 answer 올리면 안됨
# 루프 시작에서 검사 시: 예외 처리 필요 x