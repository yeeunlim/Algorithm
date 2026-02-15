def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    result = 0
    for b in babbling:
        stack = ''
        for ch in b:
            stack += ch
            if stack in words:  
                stack = ''
        if not stack:
            result += 1
            
    return result