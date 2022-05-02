# min max 문제

T = int(input())
nums_list = list(map(int, input().split()))

# 허용 정수 범위를 초과하는 값으로 비교 min과 max값 설정
min_num = 1000001
max_num = -1000001


for num in nums_list:
    if min_num > num:
        min_num = num

for num in nums_list:
    if max_num < num:
        max_num = num

print(min_num, max_num)