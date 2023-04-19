class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for i in range(len(nums)):
            if len(str(nums[i]))%2 == 0:
                even += 1
        
        return even
