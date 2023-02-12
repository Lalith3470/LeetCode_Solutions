class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        mx=0
        while start<end:
            min_storage=min(height[start],height[end])
            storage=min_storage*(end-start)
            mx=max(mx,storage)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return mx
