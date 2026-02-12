def solution(s, n):
    answer = []
    for char in s:
        if char == " ":
            answer.append(" ")
        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer.append(new_char)
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer.append(new_char)
    return "".join(answer)