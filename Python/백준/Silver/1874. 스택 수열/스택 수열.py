import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    sequence = list(map(int, input_data[1:]))
    
    stack = []
    answer = []
    current_num = 1  # 스택에 넣을 다음 숫자 (1부터 n까지)
    possible = True

    for target in sequence:
        # target 숫자가 나올 때까지 push
        while current_num <= target:
            stack.append(current_num)
            answer.append('+')
            current_num += 1
        
        # 스택의 top이 target과 같다면 pop
        if stack[-1] == target:
            stack.pop()
            answer.append('-')
        else:
            # 3. 스택의 top이 target과 다르다면 (이미 target보다 큰 값이 들어있다면) 불가능
            possible = False
            break

    if possible:
        print('\n'.join(answer))
    else:
        print('NO')

solve()