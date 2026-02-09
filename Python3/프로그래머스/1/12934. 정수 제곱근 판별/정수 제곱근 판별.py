def solution(n):
    sqrt_n = n**0.5
    if sqrt_n == int(sqrt_n):      
        return (sqrt_n + 1)**2
    else:
        return -1