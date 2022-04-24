# 3273 두 수의 합

# 실패(시간초과)
n = int(input())                                # n = 9
sequence = list(map(int, input().split(' ')))   # sequence = [5, 12, 7, 10, 9, 1, 2, 3, 11]
x = int(input())  # a1 + a2                     # x = 13

i, j, count = 0, 1, 0
while i != n:
    if j == n:
        i += 1
        j = i+1
        continue
    elif sequence[i] + sequence[j] == x:
        count += 1
        j += 1
    else:
        j += 1
print(count)

# 실패(메모리초과)
from itertools import combinations

n = int(input())
sequence = list(map(int, input().split(' ')))
x = int(input())  # a1 + a2
combi_list = list(combinations(sequence, 2))

count = 0
for i in combi_list:
    if sum(i) == 13:
        count += 1
    else:
        continue
print(count)

# 힌트 
# 포인터
# 공부하자