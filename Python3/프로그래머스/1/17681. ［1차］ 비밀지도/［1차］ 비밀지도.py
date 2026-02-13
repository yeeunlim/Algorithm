def solution(n, arr1, arr2):
    # 각 지도를 or 연산
    # bin으로 변환하고 0으로 n자리 채우기
    # '0' -> ' ', '1' -> '#'으로 변환
    return [bin(a | b)[2:].zfill(n).replace('0', ' ').replace('1', '#') for a, b in zip(arr1, arr2)]