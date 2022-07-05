# BOJ_2210 숫자판 점프
import sys

# ver 1 636ms
def dfs(x, y, digit):
    if len(digit) == 6: # 6자리 숫자이고
        if digit not in result:  # 처음 나오는 자리수이면
            result.append(digit) # 저장
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < 5 and 0 <= Y < 5: # 5*5 범위 제한
            dfs(X, Y, digit + matrix[Y][X]) # str 자리수를 걔속 더하기 '1' + '2' = '12'

matrix = [list(sys.stdin.readline().split()) for _ in range(5)]
result = []
for row in range(5):
    for col in range(5):
        dfs(col, row, matrix[row][col])
print(len(result))


# ver 2 76ms
def dfs(x, y, digit):
    if len(digit) == 6: # 6자리 숫자이고
        result.append(digit) # 저장
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < 5 and 0 <= Y < 5: # 5*5 범위 제한
            dfs(X, Y, digit + matrix[Y][X]) # str 자리수를 걔속 더하기 '1' + '2' = '12'

matrix = [list(input().split()) for _ in range(5)]
result = []
for row in range(5):
    for col in range(5):
        dfs(col, row, matrix[row][col])
result = set(result)
print(len(result))
