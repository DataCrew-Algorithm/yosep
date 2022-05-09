# 1 두수의 합

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# [실패] ver 1 투포인터
# 예외사항 : 리스트와 타겟이 음수인 경우 nums = [-1,-2,-3,-4,-5], target = -8
# from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while True:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] == target:
                return [left, right]

nums = [2,7,11,15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))


# [실패] ver 2 리스트 정렬 함수 추가
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        sorted_nums = sorted(nums)
        while True:
            if sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            elif sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            elif sorted_nums[left] + sorted_nums[right] == target:
                return [nums.index(sorted_nums[right]), nums.index(sorted_nums[left])]

nums = [-1,-2,-3,-4,-5]
target = -8

sol = Solution()
print(sol.twoSum(nums, target))


# [실패] ver 3 조합(시간초과)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, 1
        while left != len(nums)-1:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif right == len(nums)-1:
                left += 1
                right = left+1
            else:
                right += 1
sol = Solution()
print(sol.twoSum(nums, target))


# [실패] ver 4 딕셔너리 이용
# 예외사항 input = [3,3], target = 6
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[nums] = nums.index(num)
        print(nums_dict)
sol = Solution()
print(sol.twoSum(nums, target))

