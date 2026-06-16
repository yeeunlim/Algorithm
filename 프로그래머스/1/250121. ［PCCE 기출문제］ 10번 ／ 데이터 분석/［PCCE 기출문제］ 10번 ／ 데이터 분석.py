def solution(data, ext, val_ext, sort_by):
    answer = []
    columns = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    ext_col = columns[ext]
    sort_col = columns[sort_by]
    for i in range(len(data)):
        if data[i][ext_col] < val_ext:
            answer.append(data[i])
    answer = sorted(answer, key=lambda x:x[sort_col])
    return answer