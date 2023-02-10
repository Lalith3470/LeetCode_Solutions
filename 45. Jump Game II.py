class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=0,0
        steps=0
        for i in range(len(nums)-1):
            a=max(i+nums[i],a)
            if b==i:
                b=a
                steps+=1
        return steps
