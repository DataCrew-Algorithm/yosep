# 5032 탄산음료
e, f, c = map(int, (input().split()))
empty_bott = e + f  # 가지고있는 빈병
buy_list = []       # 탄산 구매 이력 저장
while empty_bott >= c:
    buy_list.append(empty_bott // c)
    empty_bott = (empty_bott // c) + (empty_bott % c) # 빈병 갯수 업데이트
    
print(sum(buy_list)) # 구매 이력 sum 출력


########################################################################
# 리스트 제거 ver
e, f, c = map(int, (input().split()))
empty_bott = e + f  # 가지고있는 빈병
buy_count = 0       # 탄산 구매 카운트

while empty_bott >= c: 
    buy_count += empty_bott // c
    empty_bott = (empty_bott // c) + (empty_bott % c) # 빈병 갯수 업데이트
    
print(buy_count)



