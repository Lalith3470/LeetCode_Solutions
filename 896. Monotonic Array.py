class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ln = nums.copy()
        ln.sort()
        return (ln==nums or ln[::-1]==nums)
        
