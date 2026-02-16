def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    result = 0
    for babble in babbling:
        stack = ''
        last_word = ''
        for char in babble:
            stack += char
            if stack in words:
                if stack != last_word:
                    last_word = stack
                    stack = ''
                else:
                    break
        if not stack:
            result += 1
            
    return result