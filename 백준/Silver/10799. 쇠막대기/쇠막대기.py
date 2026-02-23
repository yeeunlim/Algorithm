data = input()
stack = [data[0]]
answer = 0

for i in range(1, len(data)):
    if data[i] == '(':
        stack.append(data[i])
    else:
        if data[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)