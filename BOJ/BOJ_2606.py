# 2606 바이러스
from collections import deque

pc = int(input())

pairs = deque([])
for _ in range(int(input())):
    pairs.append(set(map(int, input().split())))

group_1 = {1}
for _ in range(len(pairs)*100):
    if group_1 & pairs[0]:
        group_1 = group_1 | pairs[0]
        pairs.rotate(-1)
    else:
        pairs.rotate(-1)

print(len(group_1)-1)



