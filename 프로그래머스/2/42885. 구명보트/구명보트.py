def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    boat = 0
    
    while i <= j:
        # i와 j가 같으면 혼자 남은 상황이므로 무조건 보트 +1 하고 종료
        if i == j:
            boat += 1
            break
            
        # 두 명의 합이 limit 이하일 때만 가벼운 사람(i)을 태움
        if people[i] + people[j] <= limit:
            i += 1
            
        # 무거운 사람(j)은 조건과 상관없이 항상 탑승
        j -= 1
        boat += 1
        
    return boat