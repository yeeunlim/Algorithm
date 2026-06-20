def solution(bandage, health, attacks):
    # 시전 시간, 1초당 회복량, 추가 회복량: [5, 1, 5]
    # 최대 체력: 30
    # 몬스터의 공격 시간과 피해량: [[2, 10], [9, 15], [10, 5], [11, 5]]
    
    # 공격 시간: 피해량
    # {2: 10, 9: 15, 10: 5, 11: 5}
    attack_map = dict(attacks)
    last_attack = attacks[len(attacks) - 1][0]
    curr_health = health
    streak = 0
    skill_time, heal_per_time, extra_heal = bandage

    # 체력 0 이하 되면 -1 return, 아니면 남은 체력 return
    for t in range(1, last_attack + 1):
        # 공격했으면 체력 감소, 연속 성공 초기화
        if t in attack_map:
            curr_health -= attack_map[t]
            if curr_health <= 0:
                return -1
            streak = 0
        # 공격 안했으면
        else:
            # 시전 시간 채우면 추가회복, 연속 성공 0
            if streak == skill_time:
                curr_health = min(health, curr_health + heal_per_time + extra_heal)
                streak = 0
            # 체력 회복(최대체력까지), 연속 성공 += 1
            else:
                curr_health = min(health, curr_health + heal_per_time)
        streak += 1
            
        print(t, curr_health, streak)
    return curr_health