def solution(food):
    left = ''
    for i in range(len(food)):
        n = food[i] // 2
        left += str(i) * n
    right = left[::-1]
    answer = left + '0' + right
    return answer