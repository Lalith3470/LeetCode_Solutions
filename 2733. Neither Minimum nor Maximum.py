class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums)>2:
            return nums[1]
        return -1
