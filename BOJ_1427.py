# 1427 소트인사이드
num = list(map(int, input()))
count = 0
for i in range(9, -1, -1):
    for j in num:
        if i == j:
            print(j, end='')