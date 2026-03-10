e, s, m = map(int, input().split())
n = 1
while True:
    re_e = 15 if n % 15 == 0 else n % 15
    re_s = 28 if n % 28 == 0 else n % 28
    re_m = 19 if n % 19 == 0 else n % 19
    
    if re_e == e and re_s == s and re_m == m:
        print(n)
        break
    n += 1