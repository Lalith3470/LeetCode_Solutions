class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i,k in Counter(nums).items():
            if k==1:
                return i
