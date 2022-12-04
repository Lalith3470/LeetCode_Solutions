class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set(nums)
        for i in range(1,len(nums)+2):
            if i not in num:
                return i
        
