class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*(len(nums)+1)
        mx=0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            mx=max(mx,dp[i])
        #print(dp)
        return mx
