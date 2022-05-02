# 2750 수 정렬하기

# ver 1 (실패)
# str을 sort하면 원하는 결과가 나오지 않는다. 
N = int(input())
nums = []
for _ in range(N):
    nums.append(input())

nums.sort()  # ['-1','-2','-6','1','5']

for i in range(N):
    print(nums[i])


# ver 2 (성공 116ms)
# input을 int로 다시 받아줌
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()

for i in range(N):
    print(nums[i])