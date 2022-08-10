# 1021 회전하는 큐
from collections import deque

# 2번 계산 함수
def colc_2(num, que):
    tmp = que.copy()
    cnt = 0
    while True:
        if num == tmp[0]:
            return cnt
        tmp.rotate(-1)
        cnt += 1

# 3번 계산 함수 
def colc_3(num, que):
    tmp = que.copy()
    cnt = 0
    while True:
        if num == tmp[0]:
            return cnt
        tmp.rotate(1)
        cnt += 1

N, M = map(int,input().split())
que = deque(range(1, N+1))
num = deque(map(int,input().split()))

result = 0 # 최소 계산 횟수 저장
while num: # 원하는 숫자를 전부 뽑아내면 종료
    if num[0] == que[0]: # 방법1 연산 실행
        num.popleft()
        que.popleft()
    else: 
        rotate_left = colc_2(num[0], que) # 방법2 연산 횟수 저장 
        rotate_right = colc_3(num[0], que) # 방법3 연산 횟수 저장

        # 최소한의 연산횟수 방법 체택
        if rotate_left <  rotate_right:
            result += rotate_left # 결과에 연산횟수 누적
            for _ in range(rotate_left):
                que.rotate(-1)
        else:
            result += rotate_right # 결과에 연산횟수 누적
            for _ in range(rotate_right):
                que.rotate(1)

print(result)