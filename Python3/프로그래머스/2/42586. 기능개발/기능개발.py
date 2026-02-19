import math

def solution(progresses, speeds):
    answer = []
    max_day = 0  # 현재 배포 그룹에서 가장 오래 걸리는 작업의 완료일
    
    for p, s in zip(progresses, speeds):
        # 이 작업이 끝나는 날짜 계산
        day = math.ceil((100 - p) / s)
        
        # 현재 작업이 이전 그룹의 최대 소요일보다 더 오래 걸린다면
        if day > max_day:
            answer.append(1)   # 새로운 배포 그룹 생성 (첫 번째 작업 추가)
            max_day = day      # 기준일 갱신
        else:
            # 3. 기준일 안에 끝나는 작업이면 기존 그룹에 추가
            answer[-1] += 1
            
    return answer