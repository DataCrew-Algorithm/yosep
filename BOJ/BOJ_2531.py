# 2531 회전 초밥
from collections import deque
import sys

# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split())

# 회전 초밥 리스트 생성
sushi_list = deque()
for _ in range(N):
    sushi_list.append(int(input()))

result = 0
for _ in range(len(sushi_list)): # 길이만큼 반복하면 윈위치로 rotate
    tmp = list(sushi_list)[:k] + [c] # index 0~3 초밥과 쿠폰으로 먹을 수 있는 초밥 리스트의 합
    result = max(result, len(set(tmp))) # set으로 중복 제거 후 max값으로 비교
    sushi_list.rotate(-1) # 회전

print(result)


# 슬라이딩 윈도우

import sys
from collections import defaultdict

# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.extend(arr)   # 원형이라서 2개를 이어준다.
left = 0
right = 0
dict_ = defaultdict(int)
result = 0

dict_[c] += 1          # 보너스는 무조건 먹기 
print('1dict_:', dict_)
# 1. 처음에 k 구간만큼 먹기
while right < k:
    dict_[arr[right]] += 1
    right += 1
print('dict_:', dict_)
# 2. 슬라이딩 윈도우 적용 
while right < len(arr):
    print('left', left)
    print('right', right)
    print('dict_:', dict_)
    result = max(result, len(dict_))
    print('result:', result)
    # 1. 맨 왼쪽 초밥 제거
    dict_[arr[left]] -= 1
    if dict_[arr[left]] == 0:  # 삭제된 왼쪽 초밥이 0 이면 dict 삭제 
        del dict_[arr[left]]
    # 2. 오른쪽 초밥 추가하기 
    dict_[arr[right]] += 1
    # 왼쪽 위치 + 1
    left += 1
    # 오른쪽 위치 + 1
    right += 1

print(result)