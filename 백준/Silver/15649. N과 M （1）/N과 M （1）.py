import sys

n, m = map(int, input().split())

array = []  # 현재까지 선택된 요소들을 저장하는 리스트
def backtracking():
    if len(array) == m:  # 현재까지 선택된 요소의 개수가 m과 같다면
        print(" ".join(map(str, array)))  # 현재 순열을 출력
        return  # 함수를 종료하고 돌아감

    for i in range(1, n + 1):  # 1부터 n까지 모든 숫자에 대해
        if i not in array:  # 현재 선택된 숫자들(array)에 포함되지 않은 숫자 i를 선택
            array.append(i)  # 숫자 i를 선택 (추가)
            backtracking()  # 재귀 호출을 통해 다음 숫자를 선택
            array.pop()  # 선택했던 숫자 i를 제거 (백트래킹)


backtracking()