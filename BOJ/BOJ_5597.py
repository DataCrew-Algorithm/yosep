# 5597 과제 안 내신 분

std_nums = [0]*30
for _ in range(28): # 28번의 input을 받기 위한 for문
    std_num = int(input())
    std_nums[std_num-1] = std_num # 학생번호에 맞는 index에 '학생번호'값 넣기 

for i in range(30):
    if std_nums[i] == 0:
        print(i+1) # 학생번호 = index + 1