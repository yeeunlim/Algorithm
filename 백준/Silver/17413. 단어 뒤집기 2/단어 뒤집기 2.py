import sys

def solve():
    s = sys.stdin.readline().strip()
    
    res = ""
    stack = ""
    is_tag = False

    for char in s:
        if char == "<":
            # 태그 시작 전까지 쌓인 단어가 있다면 뒤집어서 추가
            res += stack[::-1]
            stack = ""
            is_tag = True
            res += char
        elif char == ">":
            is_tag = False
            res += char
        elif is_tag:
            # 태그 내부라면 그대로 추가
            res += char
        elif char == " ":
            # 공백을 만나면 지금까지의 단어를 뒤집고 공백 추가
            res += stack[::-1] + " "
            stack = ""
        else:
            # 태그 밖 일반 문자라면 스택에 임시 저장
            stack += char

    # 반복문 종료 후 남은 단어 처리
    res += stack[::-1]
    print(res)

solve()