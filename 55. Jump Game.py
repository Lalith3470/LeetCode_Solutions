class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
        for i,val in enumerate(nums):
            if i>mx:
                return False
            mx=max(i+val,mx)
        return True
