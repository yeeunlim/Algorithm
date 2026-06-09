from collections import Counter

def solution(X, Y):
    x_count = Counter(X)
    y_count = Counter(Y)

    result = []

    for digit in "9876543210":
        count = min(x_count[digit], y_count[digit])
        result.append(digit * count)

    answer = "".join(result)

    if not answer:
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer