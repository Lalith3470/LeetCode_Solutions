class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums),2):
            b=nums[i+1]
            for i in range(nums[i]):
                l.append(b)
        return l
                
