# 1236 성 지키기

# row 기준 필요 경비원 카운트 함수
def count_empty(matrix):
    count = 0
    for i in range(len(matrix)):    # row의 수만큼 반복
        if 'X' not in matrix[i]:    # 'X'가 1개도 없으면
            count += 1              # 필요 경비원  +1
    return count

row, _ = map(int, input().split(' '))           # row의 정보만 받음
matrix = [list(input()) for _ in range(row)]    # matrix 구성

count_row = count_empty(matrix)     # row 기준 필요한 경비원 수 저장
matrix = list(zip(*matrix))         # matrix 전치
count_column = count_empty(matrix)  # column 기준 필요한 경비원 수 저장
print(max(count_row, count_column)) # 경비원의 최솟값을 출력