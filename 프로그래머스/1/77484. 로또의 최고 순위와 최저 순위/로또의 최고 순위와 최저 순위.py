def solution(lottos, win_nums):
    prize = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    win_nums = set(win_nums)
    least = 0
    zero_count = 0
    for lotto in lottos:
        if lotto in win_nums:
            least += 1
        elif lotto == 0:
            zero_count += 1
    most = least + zero_count
    return [prize[most], prize[least]]