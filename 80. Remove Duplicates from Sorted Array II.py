class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst=[]
        cnt=Counter(nums)
        for i,j in cnt.items():
            if j>2:
                lst+=[i]*2
            else:
                lst+=[i]*j
        nums[:]=lst
        return len(nums)
