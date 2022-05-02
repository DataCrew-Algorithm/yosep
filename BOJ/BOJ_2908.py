'''
# 2908 상수
nums = list(input()) # 입력받은 문자열을 리스트로 저장
nums.reverse() # 리스트열을 역순으로 변환 후 다시 저장, 반환 X
rev_nums = ''.join(nums).split() # 리스트 요소를 합친 후, split으로 다시 나눔 
print(max(map(int, rev_nums))) #str을 int형으로 변환후 두수를 비교하여 max인 값 출력

'''
# ver 2
nums = input()
rev_nums = list(reversed(nums))
sum_rev_nums = ''.join(rev_nums).split() # 리스트 요소를 합친 후, split으로 다시 나눔 
print(sum_rev_nums) #str을 int형으로 변환후 두수를 비교하여 max인 값 출력

