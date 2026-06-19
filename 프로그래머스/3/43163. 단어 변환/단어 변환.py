from collections import deque
def solution(begin, target, words):
    # begin -> words 안의 단어들을 거쳐 target으로 변환
    # bfs: 변환 가능한 노드 탐색
    # 종료: target과 같으면 종료
    # 구하는 것: 몇 번 변환해야 하는지, 변환할 수 없으면 0
    q = deque([(begin, 0)])
    visited = [False] * len(words)
    
    def can_convert(w1, w2):
        diff = 0
        for s1, s2 in zip(w1, w2):
            if s1 != s2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
    
    while q:
        curr_word, convert_count = q.popleft()
        if curr_word == target:
            return convert_count
        for i in range(len(words)):
            next_word = words[i]
            # 방문 가능하면
            if not visited[i] and can_convert(curr_word, next_word):
                q.append((next_word, convert_count + 1))
                visited[i] = True
    return 0