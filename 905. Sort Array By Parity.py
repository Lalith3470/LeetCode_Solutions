class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        m=[]
        for i in nums:
            if i%2==0:
                l.append(i)
            else:
                m.append(i)
        return l+m
