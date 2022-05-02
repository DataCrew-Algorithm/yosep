#  10798 세로읽기
matrix = []

for i in range(5):
    row = []
    for j in range(15):
        row.append('')
    matrix.append(row)


for i in range(5):
    word = input()
    for j in range(len(word)):
        matrix[i][j] = word[j]

unpack_matrix = list(map(list, zip(*matrix)))


for i in range(15):
    one_line =+ unpack_matrix[i]

print(one_line)