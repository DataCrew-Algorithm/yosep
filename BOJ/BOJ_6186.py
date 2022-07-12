# 6186 Best Grass
from collections import deque 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    graph[y][x] = 0
    queue = deque([x, y])
    while queue:
        a, b = queue[0][0], queue[0][1]
        queue.popleft()
        for i in range(4):
            X = a + dx[i]
            Y = b + dy[i]
            if 0 <= X < col and 0 <= Y < row:
                if graph[Y][X] == '#':
                    graph[Y][X] = 0
                    queue.append([X, Y])
    return


row, col = map(int, input().split())
graph = [list(input()) for _ in range(row)]

result = 0
for r in range(row):
    for c in range(col):
        if graph[r][c] == '#':
            dfs(c, r)
            result += 1
print(result)
