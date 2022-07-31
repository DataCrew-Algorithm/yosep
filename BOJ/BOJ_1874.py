# 1874 스택 수열
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
init = deque(list(range(1,N+1)))

target = deque()
for _ in range(N):
    target.append(int(input()))

stack = []
log = []
for _ in range(N*2): # 최대 연산 가능 횟수
    if stack and stack[-1] == target[0]: # stack 값이 존재하고 수열과 일치한다면
        stack.pop()
        target.popleft()
        log.append('-') # 연산 로그 저장
        continue
    if init:
        stack.append(init.popleft())
        log.append('+')

if len(log) == N*2: # 예상 연산횟수와 일치한 경우
    for i in log:
        print(i)
else:
    print('No')