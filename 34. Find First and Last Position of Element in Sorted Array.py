class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        s=[]
        nums.sort()
        for i in range(len(nums)):
            if target>=nums[i]:
                if target==nums[i]:
                    l.append(i)
        if len(l)>1:
            s.append(l[0])
            s.append(l[-1])
            return s
        elif len(l)==1:
            l.append(l[0])
            return l
        else:
            return [-1,-1]
