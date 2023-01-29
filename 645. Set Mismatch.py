class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                l.append(nums[i])
        for i in range(len(nums)):
            if i+1 not in nums:
                return l+[i+1]
