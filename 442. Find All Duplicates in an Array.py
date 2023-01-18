class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                l.append(nums[i])
        return set(l)
