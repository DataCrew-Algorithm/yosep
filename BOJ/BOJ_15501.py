# BOJ_15501 부당한 퍼즐
from collections import deque

N = int(input())       
sequence_1 = deque(input().split())                 # deque(['1', '2', '3', '4', '5'])
reversed_sequence_1 = deque(reversed(sequence_1))   # deque(['5', '4', '3', '2', '1'])
sequence_2 = deque(input().split())                 # deque(['4', '3', '2', '1', '5'])

for _ in range(N):
    if sequence_1 == sequence_2 or reversed_sequence_1 == sequence_2:
        print('good puzzle')
        break
    sequence_1.rotate(1)   # deque를 한칸씩 오른쪽으로 이동 
    reversed_sequence_1.rotate(1)
else:
    print('bad puzzle')