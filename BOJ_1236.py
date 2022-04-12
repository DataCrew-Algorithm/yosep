# 1236 성 지키기
def count_empty(matrix):
    count = 0
    for i in range(len(matrix)):
        if 'X' not in matrix[i]:
            count += 1
    return count

row, _ = map(int, input().split(' '))
matrix = [list(input()) for _ in range(row)]

count_row = count_empty(matrix)
matrix = list(zip(*matrix))
count_column = count_empty(matrix)
print(max(count_row, count_column))