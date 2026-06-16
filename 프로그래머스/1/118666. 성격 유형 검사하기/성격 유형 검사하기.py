def solution(survey, choices):
    choices_score = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: -1,
        6: -2,
        7: -3
    }
    scores = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}
    for s, c in zip(survey, choices):
        sorted_s = ''.join(sorted(s))
        if s == sorted_s:
            scores[sorted_s] += choices_score[c]
        else:
            scores[sorted_s] -= choices_score[c]
    answer = ''
    for key in scores.keys():
        if scores[key] >= 0:
            answer += key[0]
        else:
            answer += key[1]
    return answer
            