class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm=nums[0]
        subsum=0
        for num in nums:
            subsum+=num
            sm=max(sm,subsum)
            if subsum<=0:
                subsum=0
        return sm 
