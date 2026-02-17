from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    n = len(a_to_z)

    dict_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    return "".join(a_to_z[(dict_alpha[char] + index) % n] for char in s)