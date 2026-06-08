def solution(diffs, times, limit):
    def can_solve(level):
        total_time = times[0]
        for i in range(1, len(diffs)):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                mistakes = diffs[i] - level
                total_time += mistakes * (times[i] + times[i - 1]) + times[i]
            
        if total_time > limit:
            return False
        return True
    
    low, high = 1, max(diffs)
    while low < high:
        mid = (low + high) // 2
        
        if can_solve(mid):
            high = mid
        else:
            low = mid + 1
    return low
            

            
        