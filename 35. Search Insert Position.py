class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
            elif i+1 == len(nums) and target>nums[i]:
                return i+1
