def solution(k, m, score):
    score.sort(reverse=True)
    boxes = []
    div = len(score) // m
    for i in range(0, div):
        boxes.append(score[i*m:(i+1)*m])
    return sum([min(box)*m for box in boxes])