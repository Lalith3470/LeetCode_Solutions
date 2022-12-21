class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = [*set(nums)]
        l.sort()
        for i in range(len(nums)):
            if l[-1]==nums[i]:
                return i
