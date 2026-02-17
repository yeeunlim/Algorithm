from collections import Counter

def solution(N, stages):
    failure_rate = {}
    fail_players = Counter(stages)
    total_players = len(stages)
    
    for i in range(1, N+1):
        if total_players > 0:
            failure_rate[i] = fail_players[i] / total_players
            total_players -= fail_players[i]
        else:
            failure_rate[i] = 0
    
    print(failure_rate)
    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)