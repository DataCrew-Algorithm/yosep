# 1427 소트인사이드
num = list(map(int, input()))   # input N의 자리수를 순서대로 list에 저장
for i in range(9, -1, -1):      # 9~0 큰수부터 순서대로 비교
    for j in num:               # j는 각 자리수에 해당
        if i == j: 
            print(j, end='')    #큰수부터 차례대로 출력