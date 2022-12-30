class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj=len(nums)//3
        l={}
        lst=[]
        for i in nums:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for i,j in l.items():
            if j>maj:
                lst.append(i)
        return lst
