class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = set(range(1, len(nums)+1))
        return list(result - set(nums))
