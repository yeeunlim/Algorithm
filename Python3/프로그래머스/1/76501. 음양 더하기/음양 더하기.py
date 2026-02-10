def solution(absolutes, signs):
    sum = 0
    for ab, sign in zip(absolutes, signs):
        if sign == True:
            sum += ab
        else:
            sum += (-1)*ab
    return sum