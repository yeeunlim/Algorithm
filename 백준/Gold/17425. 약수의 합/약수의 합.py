import sys

def solve():
    MAX = 1000000
    # f[i]: i의 약수의 합
    f = [1] * (MAX + 1)
    # g[i]: f[1] + f[2] + ... + f[i]
    g = [0] * (MAX + 1)

    # f(n) 계산
    # i는 약수, j는 i를 약수로 가지는 수 (i의 배수)
    for i in range(2, MAX + 1):
        for j in range(i, MAX + 1, i):
            f[j] += i

    # g(n) 계산
    for i in range(1, MAX + 1):
        g[i] = g[i-1] + f[i]

    # 테스트 케이스 처리
    input_data = sys.stdin.read().split()

    t = int(input_data[0])
    queries = input_data[1:]
    
    # 결과를 리스트에 모아서 한 번에 출력
    answers = []
    for i in range(t):
        n = int(queries[i])
        answers.append(str(g[n]))
    
    sys.stdout.write('\n'.join(answers) + '\n')

if __name__ == '__main__':
    solve()