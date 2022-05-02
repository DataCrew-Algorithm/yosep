# 3273 두 수의 합

# 실패(시간초과)
n = int(input())                                # n = 9
sequence = list(map(int, input().split(' ')))   
x = int(input())  # a1 + a2                     # x = 13
# sequence = [5, 12, 7, 10, 9, 1, 2, 3, 11] 
i, j, count = 0, 1, 0   # 초기값으로 i, j 각각 index 0번과 1번자리
while i != n:           # nC2 구현 반복문
    if j == n:          
        i += 1
        j = i+1
    elif sequence[i] + sequence[j] == x:
        count += 1      #  조합의 합이 x이면 count + 1
        j += 1
    else:
        j += 1
print(count)

# 실패(메모리초과)
from itertools import combinations

n = int(input())
sequence = list(map(int, input().split(' ')))
x = int(input()) 
combi_list = list(combinations(sequence, 2))

count = 0
for i in combi_list:
    if sum(i) == x:
        count += 1
print(count)

# 힌트 : 투 포인터
# 그 외 풀이 : 수학적 접근
# 결론 >>> 수학은 대단하다...