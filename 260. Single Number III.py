class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l={}
        lst=[]
        for i in nums:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for i,j in l.items():
            if j==1:
                lst.append(i)
        return lst
