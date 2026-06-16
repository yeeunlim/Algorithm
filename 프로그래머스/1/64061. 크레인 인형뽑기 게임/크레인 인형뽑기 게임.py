def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            curr_grid = board[i][move - 1]
            # 인형이 없으면 계속 내려감
            if curr_grid == 0:
                continue
            else:
                # 제일 위에 있는 인형 집기
                board[i][move - 1] = 0
                # 스택 맨 위랑 같으면 인형 터뜨리기
                if stack and stack[-1] == curr_grid:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(curr_grid)
                break
    return answer