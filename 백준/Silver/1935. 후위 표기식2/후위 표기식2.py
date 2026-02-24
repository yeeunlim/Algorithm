import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    expression = input_data[1]
    # 알파벳 순서대로 들어오는 숫자들을 리스트에 저장
    values = [int(x) for x in input_data[2:]]
    
    stack = []
    
    for char in expression:
        # A-Z 문자인 경우
        if 'A' <= char <= 'Z':
            # 'A'는 0번 인덱스, 'B'는 1번 인덱스로 매핑
            stack.append(values[ord(char) - ord('A')])
        else:
            # 연산자를 만난 경우 (먼저 꺼낸 것이 오른쪽 피연산자)
            num2 = stack.pop()
            num1 = stack.pop()
            
            if char == '+':
                stack.append(num1 + num2)
            elif char == '-':
                stack.append(num1 - num2)
            elif char == '*':
                stack.append(num1 * num2)
            elif char == '/':
                stack.append(num1 / num2)

    # 3. 결과 출력 (소수점 둘째 자리까지 고정)
    print(f"{stack[0]:.2f}")

if __name__ == "__main__":
    solve()