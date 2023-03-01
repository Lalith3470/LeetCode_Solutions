class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums1=nums.copy()
        nums1.sort()
        if nums1[-1]>=nums1[-2]*2:
            for i in range(len(nums)):
                if nums1[-1]==nums[i]:
                    return i
        else:
            return -1
