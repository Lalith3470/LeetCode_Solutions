class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                l.append(count)
                count=0
            else:
                count+=1
        l.append(count)
        
        return max(l)
