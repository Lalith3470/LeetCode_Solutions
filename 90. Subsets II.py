class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        nums.sort()
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                lst.append(j)
        return set(lst)
       
