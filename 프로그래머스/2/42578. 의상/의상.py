def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        clothes_dict[cloth[1]] = clothes_dict.get(cloth[1], 1) + 1
    count = clothes_dict.values()
    
    for c in count:
        answer *= c
        
    return answer - 1