class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = permutations(nums)
        lst=[]
        for num in nums:
            if num not in lst:
                lst.append(num)
        return lst
