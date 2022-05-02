# 3040 백설 공주와 일곱 난쟁이
nums = []
for _ in range(9):
    nums.append(int(input()))

for i in range(8): # 9개중 2개를 택하는 조합 (nCr) 
    for j in range(i+1, 9):
        if sum(nums) - (nums[i]+nums[j]) == 100: # 뽑은 두 수를 빼서 합이 100이면
            nums[i] = 0
            nums[j] = 0
            break

for num in nums:
    if num > 0:
        print(num)


# for문을 통한 nCr 코드의 한계
# 만일 필요없는 수가 2개가 아니라 그보다 더 큰 수라면?