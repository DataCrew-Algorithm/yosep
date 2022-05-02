# 2456 나는 학급회장이다(실패)

def max_index(x): # list의 max값이 유일하면 index반환하는 함수 
    max_num = max(x)
    if x.count(max_num) == 1:
        return x.index(max_num)
    else:
        return -1


# 선호도 리스트
t = [[], [], []]  # 1번후보 = t[0], 2번후보 = t[1], 3번후보 = t[2]

# 후보별 선호도 입력 반복문
N = int(input())
for i in range(N): 
    pref1, pref2, pref3 = map(int, input().split())
    t[0].append(pref1)
    t[1].append(pref2)
    t[2].append(pref3) 

# 총합
sum_nums = [sum(t[0]), sum(t[1]), sum(t[2])]
max_num = max(sum_nums)

# 선호도 카운트 리스트
count_3_point = [0, 0, 0]
count_2_point = [0, 0, 0]
count_1_point = [0, 0, 0]

for i in range(3):
    count_3_point[i] = t[i].count(3)
    count_2_point[i] = t[i].count(2)
    count_1_point[i] = t[i].count(1)


if max_index(sum_nums) >= 0: # max가 유일한 경우
    print(f'{max_index(sum_nums)+1} {max_num}')
else: # max가 유일하지 않을 때
    if max_index(count_3_point) >= 0: # 호감도 3의 count가 가장많은 후보
        print(f'{max_index(count_3_point)+1} {max_num}')
    elif max_index(count_2_point) >= 0: # 호감도 2의 count가 가장많은 후보
        print(f'{max_index(count_2_point)+1} {max_num}')
    else: # 그 외
        print(f'0 {max_num}')