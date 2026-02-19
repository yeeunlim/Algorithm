import re

def solution(dartResult):
    pattern = re.compile(r'(\d+)([SDT])([*#]?)')
    darts = pattern.findall(dartResult)
    scores = []

    for score, bonus, option in darts:
        point = int(score)
        
        if bonus == 'S': point **= 1
        elif bonus == 'D': point **= 2
        elif bonus == 'T': point **= 3
        
        if option == '*':
            point *= 2
            if scores:
                scores[-1] *= 2
        elif option == '#':
            point *= -1
            
        scores.append(point)
        
    return sum(scores)