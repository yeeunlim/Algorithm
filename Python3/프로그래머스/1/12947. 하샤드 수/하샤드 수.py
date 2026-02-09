def solution(x):
    sum_num = sum(map(int, list(str(x))))
    
    # if문 전체를 리턴문으로 축약 가능
    return x % sum_num == 0