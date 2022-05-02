# 5800 성적 통계

# 리스트의 연속되는 두 수의 차 중, 가장 큰 수를 반환하는 함수
def largest_gap(list):
    tmp = []
    for i in range(len(list)-1):
        tmp.append(list[i+1]-list[i])
    return max(tmp)

for i in range(int(input())): # 교실 수 만큼 반복
    students = list(map(int, input().split()))[1:] # 학생 수(index[0])을 제외하여 리스트에 저장 [5 30 25 76 23 78] -> [30 25 76 23 78]
    students.sort() # 점수 정렬
    print(f'Class {i+1}\nMax {students[-1]}, Min {students[0]}, Largest gap {largest_gap(students)}')

# ex) input
# 2
# 5 30 25 76 23 78
# 6 25 50 70 99 70 90

# ex) output
# Class 1
# Max 78, Min 23, Largest gap 46
# Class 2
# Max 99, Min 25, Largest gap 25