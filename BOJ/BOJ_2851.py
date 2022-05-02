# 2851 슈퍼 마리오
nums = []
for _ in range(10):
    nums.append(int(input()))
    
sum_point = 0
compare_point = 0

for i in range(10):
    sum_point += nums[i] # 앞에서부터 차례대로 더하기
    if sum_point == 100: # 정확히 100
        break
    elif sum_point > 100: # sum이 100을 넘기면
        compare_point = sum_point - nums[i] # (i-1)번째 sum 결과를 compare에 저장하고 break 
        break
        
if (sum_point - 100) <= (100 - compare_point):  # 1. sum이 정확히 100이면 print(sum_point)
    print(sum_point)                            # 2. 100에 더 가까우면 print(sum_point) 
else:                                           # 3. 똑같이 가까우면 print(sum_point)
    print(compare_point)