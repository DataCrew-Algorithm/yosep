#지능형 기차
train = 0 # 열차 사람 수
sum_passengers = [0]*4 # 각 역 별 승객 합

for _ in range(4): 
    out_count, in_count = map(int, input().split()) # 정차역의 하차, 승차 승객 수 저장
    train += -out_count + in_count # 정차역의 총 승객수 합 계산
    sum_passengers.append(train) # 각 역의 승객수의 합을 리스트에 저장
    
print(max(sum_passengers)) # 저장된 역 별 승객수 합 중에 가장 큰 수 출력