def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack: 
                return False  # ')'로 시작하면 올바르지 않은 괄호
            else:
                stack.pop()  # 짝이 맞는 괄호를 pop
    
    return len(stack) == 0  # 짝이 맞아떨어지면 True, 짝이 맞지 않아 남는 괄호가 있으면 False