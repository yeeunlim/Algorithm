import sys
from collections import Counter

input = sys.stdin.read
data = input().split()

n = int(data[0])
nums = list(map(int, data[1:]))
count = Counter(nums)

stack = []
answer = [-1] * n

for i in range(n):
    # 스택이 비어있지 않고, 현재 숫자의 빈도수가 스택 top에 있는 숫자의 빈도수보다 클 때
    while stack and count[nums[stack[-1]]] < count[nums[i]]:
        index = stack.pop()
        answer[index] = nums[i]
    
    stack.append(i)

print(*(answer))