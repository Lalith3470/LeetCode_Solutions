class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        m=[]
        for ele in nums:
            if ele==0:
                l.append(0)
            else:
                m.append(ele)
                
        nums[:]=m+l
