class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = [*set(nums)]
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        
        a = nums[len(nums)-1]
        
        return a+1
