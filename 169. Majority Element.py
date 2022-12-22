class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=sorted(nums)
        i=0
        for _ in range(len(set(n))):
            if n.count(n[i])>=len(n)/2: 
                return n[i]
            else: 
                i=i+n.count(n[i])
            
