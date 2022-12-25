class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        dupl = [*set(nums)]
        return a == len(dupl)
