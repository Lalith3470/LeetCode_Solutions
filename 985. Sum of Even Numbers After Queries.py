class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        sm=0
        for i in nums: 
            if i%2==0: 
                sm+= i
        for val in queries:
            if nums[val[1]]%2==0: 
                sm-=nums[val[1]]
            nums[val[1]]+=val[0]
            if nums[val[1]]%2==0: 
                sm+=nums[val[1]]
            res.append(sm)
        return res
