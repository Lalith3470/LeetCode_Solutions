class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=prod(nums)
        n=nums.copy()
        s=[]
        for i in nums:
            if i==0:
                n.remove(i)
                s.append(prod(n))
                n=nums.copy()
            else:
                s.append(int(l/i))
        return s        
        
