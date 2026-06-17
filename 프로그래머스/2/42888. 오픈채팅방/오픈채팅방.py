def solution(record):
    # {uid: nickname}
    users = {}
    # ['users[uid1]님이 들어왔습니다.', 'users[uid2]님이 나갔습니다.', ...]
    messages = []
    # 닉네임 저장/변경
    for rec in record:
        rec_split = rec.split()
        uid = rec_split[1]
        if rec_split[0] == 'Enter':
            nickname = rec_split[2]
            users[uid] = nickname
        elif rec_split[0] == 'Change':
            nickname = rec_split[2]
            users[uid] = nickname
    
    # 입장/퇴장 메시지 저장
    for rec in record:
        rec_split = rec.split()
        uid = rec_split[1]
        if rec_split[0] == 'Enter':
            messages.append(f'{users[uid]}님이 들어왔습니다.')
        elif rec_split[0] == 'Leave':
            messages.append(f'{users[uid]}님이 나갔습니다.')
    return messages