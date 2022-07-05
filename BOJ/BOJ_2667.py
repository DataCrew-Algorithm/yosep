# 2667 단지번호붙이기
import numpy as np

# 시계방향(상우하좌)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = [[x, y]]
    cnt = 0 # 단지내 집 개수 카운트
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            X = a + dx[i]
            Y = b + dy[i]
            if 0 <= X < N and 0 <= Y < N and matrix[Y][X] == 1:
                matrix[Y][X] = 0
                cnt += 1
                queue.append([X, Y])
    return cnt

N = int(input())
house = [] # 단지내 집 개수를 저장할 리스트
matrix = [list(map(int, input())) for _ in range(N)]
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1:
            def_return = bfs(col, row)
            if def_return == 0:
                house.append(1)
            else:
                house.append(def_return)
            # house.append(bfs(col, row))
            matrix[row][col] = 0

print(len(house))
for i in sorted(house):
    print(i)


#####################################################################