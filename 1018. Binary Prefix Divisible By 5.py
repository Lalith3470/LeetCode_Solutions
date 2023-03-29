class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        l=[]
        s=""
        for i in nums:
            s+=str(i)
            l.append(int(s,2)%5==0)
        return l
