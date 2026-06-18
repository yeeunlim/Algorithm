def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        to_remove = find_blocks(board)

        if not to_remove:
            break

        answer += len(to_remove)
        remove_blocks(board, to_remove)
        drop_blocks(board)

    return answer


def find_blocks(board):
    to_remove = set()

    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            if board[i][j] != '' and (
                board[i][j] == board[i][j + 1] ==
                board[i + 1][j] == board[i + 1][j + 1]
            ):
                to_remove.update([
                    (i, j),
                    (i, j + 1),
                    (i + 1, j),
                    (i + 1, j + 1)
                ])

    return to_remove


def remove_blocks(board, to_remove):
    for x, y in to_remove:
        board[x][y] = ''


def drop_blocks(board):
    for j in range(len(board[0])):
        blocks = []

        for i in range(len(board)):
            if board[i][j] != '':
                blocks.append(board[i][j])

        empty_count = len(board) - len(blocks)

        for i in range(empty_count):
            board[i][j] = ''

        for i in range(empty_count, len(board)):
            board[i][j] = blocks[i - empty_count]