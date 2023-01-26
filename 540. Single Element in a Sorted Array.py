class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dict=Counter(nums)
        for i in sorted(dict, key=dict.get):
            return i
